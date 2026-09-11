param([string]$Engine = 'pdflatex')
$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$bundleDir = Join-Path $repoRoot 'paper_assets/v2/arxiv_submission'
$inputs = @(Get-ChildItem -LiteralPath $bundleDir -Force)
if ($inputs.Count -ne 1 -or $inputs[0].Name -ne 'ringmin_v2.tex' -or
    $inputs[0].PSIsContainer) { throw 'Bundle must contain only ringmin_v2.tex' }
$sourceHash = (Get-FileHash -LiteralPath $inputs[0].FullName -Algorithm SHA256).Hash
$candidateHash = (Get-FileHash -LiteralPath (Join-Path $repoRoot 'paper_assets/v2/ringmin_v2.tex') -Algorithm SHA256).Hash
if ($sourceHash -ne $candidateHash) { throw 'Bundle and candidate source differ' }
$buildDir = Join-Path $repoRoot ('reproducibility/.work/arxiv-clean-' + [guid]::NewGuid().ToString('N'))
$null = New-Item -ItemType Directory -Path $buildDir
Copy-Item -LiteralPath $inputs[0].FullName -Destination $buildDir
if (@(Get-ChildItem -LiteralPath $buildDir -Force).Count -ne 1) {
    throw 'Clean directory contains extra inputs'
}
$savedEpoch = $env:SOURCE_DATE_EPOCH
$savedForce = $env:FORCE_SOURCE_DATE
$savedInputs = $env:TEXINPUTS
$env:SOURCE_DATE_EPOCH = '1789084800'
$env:FORCE_SOURCE_DATE = '1'
$env:TEXINPUTS = '.;'
$stable = $false
$previous = ''
Push-Location $buildDir
try {
    for ($pass = 1; $pass -le 4; $pass++) {
        & $Engine -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder ringmin_v2.tex > ('pass-' + $pass + '.txt') 2>&1
        $compileExit = $LASTEXITCODE
        if ($compileExit -ne 0) { throw "pdflatex pass $pass exited $compileExit" }
        $referenceHashes = @('ringmin_v2.aux', 'ringmin_v2.out') | ForEach-Object {
            (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash
        }
        $current = $referenceHashes -join ':'
        Write-Output "PASS pdflatex pass $pass exit=0"
        if ($pass -ge 3 -and $current -eq $previous) { $stable = $true; break }
        $previous = $current
    }
    if (-not $stable) { throw 'References did not stabilize within four passes' }
    $log = Get-Content -LiteralPath 'ringmin_v2.log' -Raw
    $failures = 'Overfull |Underfull |Missing character|undefined|multiply defined|Rerun to get|Label\(s\) may have changed|Package .* Warning|LaTeX Warning|destination with the same identifier'
    if ($log -match $failures) { throw 'Final TeX log requires review' }
    Write-Output 'PASS stable aux/out; no reference, citation, glyph, box or package warnings'
    $relative = $buildDir.Substring($repoRoot.Length + 1).Replace('\', '/')
    Write-Output ('CLEAN_BUILD=' + $relative)
    Write-Output ('SOURCE_SHA256=' + $sourceHash.ToLowerInvariant())
    Write-Output ('PDF_SHA256=' + (Get-FileHash -LiteralPath 'ringmin_v2.pdf' -Algorithm SHA256).Hash.ToLowerInvariant())
} finally {
    Pop-Location
    $env:SOURCE_DATE_EPOCH = $savedEpoch
    $env:FORCE_SOURCE_DATE = $savedForce
    $env:TEXINPUTS = $savedInputs
}
