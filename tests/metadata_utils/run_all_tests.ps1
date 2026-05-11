$ScriptDir = Split-Path $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path "$ScriptDir\..\.."

# Try to find activation script (handle Windows vs Unix paths if running pwsh on Unix)
$WinActivate = Join-Path $ProjectRoot "wsheet-env\Scripts\Activate.ps1"
$UnixActivate = Join-Path $ProjectRoot "wsheet-env/bin/Activate.ps1"

if (Test-Path $WinActivate) {
    . $WinActivate
} elseif (Test-Path $UnixActivate) {
    . $UnixActivate
} else {
    Write-Host "Warning: Could not find virtual environment activation script."
}

Write-Host "Running all tests in tests/metadata_utils with virtualenv..."
pytest $ScriptDir
