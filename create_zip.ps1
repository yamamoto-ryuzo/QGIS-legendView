# PowerShell script to create plugin ZIP package
# This script creates a distribution ZIP file for the QGIS plugin

$PLUGIN_NAME = "legend_view"
$ZIP_NAME = "$PLUGIN_NAME.zip"

Write-Host "Creating plugin ZIP package: $ZIP_NAME"

# Remove existing ZIP file if it exists
if (Test-Path $ZIP_NAME) {
    Remove-Item $ZIP_NAME -Force
    Write-Host "Removed existing ZIP file"
}

# Define files to include in the ZIP
$FILES_TO_INCLUDE = @(
    "__init__.py",
    "legend_view.py",
    "legend_view_dockwidget.py",
    "legend_view_dockwidget_base.ui",
    "resources_rc.py",
    "metadata.txt",
    "icon.png",
    "legend.png"
)

# Define directories to include
$DIRS_TO_INCLUDE = @(
    "i18n",
    "legend"
)

# Create temporary directory for ZIP contents
$TEMP_DIR = "temp_$PLUGIN_NAME"
if (Test-Path $TEMP_DIR) {
    Remove-Item $TEMP_DIR -Recurse -Force
}
New-Item -ItemType Directory -Path $TEMP_DIR | Out-Null
New-Item -ItemType Directory -Path "$TEMP_DIR\$PLUGIN_NAME" | Out-Null

Write-Host "Copying files to temporary directory..."

# Copy files
foreach ($file in $FILES_TO_INCLUDE) {
    if (Test-Path $file) {
        Copy-Item $file "$TEMP_DIR\$PLUGIN_NAME\" -Force
        Write-Host "✓ Copied: $file"
    } else {
        Write-Host "✗ Not found: $file"
    }
}

# Copy directories
foreach ($dir in $DIRS_TO_INCLUDE) {
    if (Test-Path $dir) {
        Copy-Item $dir "$TEMP_DIR\$PLUGIN_NAME\" -Recurse -Force
        Write-Host "✓ Copied directory: $dir"
    } else {
        Write-Host "✗ Directory not found: $dir"
    }
}

# Create ZIP file
Write-Host "Creating ZIP archive..."
try {
    Compress-Archive -Path "$TEMP_DIR\$PLUGIN_NAME" -DestinationPath $ZIP_NAME -Force
    Write-Host "✓ Successfully created: $ZIP_NAME"
    
    # Get file size
    $zipSize = (Get-Item $ZIP_NAME).Length
    $zipSizeKB = [math]::Round($zipSize / 1024, 2)
    Write-Host "   File size: $zipSizeKB KB"
    
} catch {
    Write-Host "✗ Error creating ZIP file: $($_.Exception.Message)"
    exit 1
}

# Clean up temporary directory
Remove-Item $TEMP_DIR -Recurse -Force
Write-Host "✓ Cleaned up temporary files"

Write-Host ""
Write-Host "Plugin ZIP package created successfully!"
Write-Host "File: $ZIP_NAME"
Write-Host "Ready for distribution or upload to QGIS Plugin Repository"
