param(
    [int]$Start = 12,
    [int]$Stop = 12,
    [int]$K = 20000,
    [int]$Workers = 8,
    [switch]$Resume
)

$Root = Split-Path -Parent $PSScriptRoot
$LogDir = Join-Path $Root "results\logs"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$Stdout = Join-Path $LogDir "sweep_${Start}_${Stop}_${Stamp}.out.log"
$Stderr = Join-Path $LogDir "sweep_${Start}_${Stop}_${Stamp}.err.log"

$Args = @(
    "scripts/sweep_certified.py",
    "--start", "$Start",
    "--stop", "$Stop",
    "--k", "$K",
    "--workers", "$Workers"
)
if ($Resume) {
    $Args += "--resume"
}

Start-Process `
    -FilePath "python" `
    -ArgumentList $Args `
    -WorkingDirectory $Root `
    -RedirectStandardOutput $Stdout `
    -RedirectStandardError $Stderr `
    -WindowStyle Hidden

Write-Output "Started detached sweep. stdout=$Stdout stderr=$Stderr"
