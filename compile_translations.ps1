# PowerShell script to compile translation files
# Run this script to compile .ts files to .qm files

Write-Host "Compiling translation files..."

# Check if lrelease is available
if (Get-Command lrelease -ErrorAction SilentlyContinue) {
    Write-Host "Found lrelease, compiling translations..."
    
    # Compile Japanese translation
    if (Test-Path "i18n\LegendView_ja.ts") {
        lrelease "i18n\LegendView_ja.ts"
        Write-Host "✓ Japanese translation compiled"
    } else {
        Write-Host "✗ Japanese translation file not found"
    }
    
    # Compile English translation
    if (Test-Path "i18n\LegendView_en.ts") {
        lrelease "i18n\LegendView_en.ts"
        Write-Host "✓ English translation compiled"
    } else {
        Write-Host "✗ English translation file not found"
    }
    
    Write-Host "Translation compilation completed!"
} else {
    Write-Host "Error: lrelease not found. Please make sure Qt tools are installed and in your PATH."
    Write-Host "You may need to install Qt or add Qt bin directory to your PATH."
    exit 1
}
