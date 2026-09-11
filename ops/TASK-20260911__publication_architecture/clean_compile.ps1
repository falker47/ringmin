param([ValidateSet('sequel','correction')][string]$Candidate,
      [string]$Engine = 'pdflatex')
$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
if ($Candidate -eq 'sequel') {
    $relativeBundle = 'paper_assets/asymptotic_sequel/source_bundle'
    $stem = 'ringmin_asymptotic'
    $expectedCount = 1
} else {
    $relativeBundle = 'paper_assets/v1_correction/source_bundle'
    $stem = 'ringmin_finite_v2'
    $expectedCount = 4
}
$bundleDir = Join-Path $repoRoot $relativeBundle
$inputs = @(Get-ChildItem -LiteralPath $bundleDir -Recurse -File -Force)
if ($inputs.Count -ne $expectedCount) { throw 'Unexpected source inventory' }
$buildDir = Join-Path $repoRoot ('reproducibility/.work/independent-' + $Candidate + '-' + [guid]::NewGuid().ToString('N'))
$null = New-Item -ItemType Directory -Path $buildDir
foreach ($inputFile in $inputs) {
    $relative = $inputFile.FullName.Substring($bundleDir.Length + 1)
    $destination = Join-Path $buildDir $relative
    $null = New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force
    Copy-Item -LiteralPath $inputFile.FullName -Destination $destination
}
$savedEpoch = $env:SOURCE_DATE_EPOCH
$savedForce = $env:FORCE_SOURCE_DATE
$savedInputs = $env:TEXINPUTS
$env:SOURCE_DATE_EPOCH = '1789084800'
$env:FORCE_SOURCE_DATE = '1'
$env:TEXINPUTS = '.;'
$previous = ''
$stable = $false
Push-Location $buildDir
try {
    for ($pass = 1; $pass -le 5; $pass++) {
        & $Engine -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder ($stem + '.tex') > ('pass-' + $pass + '.txt') 2>&1
        if ($LASTEXITCODE -ne 0) { throw "pdflatex pass $pass exited $LASTEXITCODE" }
        $current = @('.aux','.out') | ForEach-Object {
            (Get-FileHash -LiteralPath ($stem + $_) -Algorithm SHA256).Hash
        }
        $current = $current -join ':'
        if ($pass -ge 3 -and $current -eq $previous) { $stable = $true; break }
        $previous = $current
    }
    if (-not $stable) { throw 'Unstable references' }
    $log = Get-Content -LiteralPath ($stem + '.log') -Raw
    if ($log -match 'Overfull |Underfull |Missing character|undefined|multiply defined|Rerun to get|Label\(s\) may have changed|Package .* Warning|LaTeX Warning|destination with the same identifier') {
        throw 'Final TeX log requires review'
    }
    Write-Output "PASS independent $Candidate compile; $expectedCount inputs; $pass passes; zero warnings"
    Write-Output ('CLEAN_BUILD=' + $buildDir.Substring($repoRoot.Length + 1).Replace('\','/'))
} finally {
    Pop-Location
    $env:SOURCE_DATE_EPOCH = $savedEpoch
    $env:FORCE_SOURCE_DATE = $savedForce
    $env:TEXINPUTS = $savedInputs
}
