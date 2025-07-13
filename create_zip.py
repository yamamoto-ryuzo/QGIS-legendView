#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QGIS Plugin ZIP Package Creator
Creates a distribution ZIP file for the QGIS Legend View plugin
"""

import os
import zipfile
import shutil
import configparser
from pathlib import Path

# Import version information
try:
    from version import __version__, get_version_info
    PLUGIN_VERSION = __version__
except ImportError:
    PLUGIN_VERSION = "2.0.1"

def get_plugin_name_from_metadata():
    """Read plugin name from metadata.txt"""
    try:
        config = configparser.ConfigParser()
        config.read('metadata.txt', encoding='utf-8')
        return config.get('general', 'name')
    except Exception as e:
        print(f"Warning: Could not read plugin name from metadata.txt: {e}")
        return "QGIS-legendView"  # fallback name

def create_plugin_zip():
    """Create ZIP package for QGIS plugin distribution"""
    
    # Read plugin name from metadata.txt
    plugin_folder_name = get_plugin_name_from_metadata()
    REPO_NAME = "QGIS_legendView"  # Repository name with - replaced by _
    ZIP_NAME = f"{REPO_NAME}_v{PLUGIN_VERSION}.zip"
    
    # Files to include in the ZIP
    FILES_TO_INCLUDE = [
        "__init__.py",
        "legend_view.py", 
        "legend_view_dockwidget.py",
        "legend_view_dockwidget_base.ui",
        "resources_rc.py",
        "metadata.txt",
        "LICENSE",
        "README.md",
        "icon.png",
        "legend.png",
        "qt_compat.py",
        "version.py",
        "CHANGELOG.md",
        "create_translations.py",
        "version_manager.py",
        "validate_package.py"
    ]
    
    # Directories to include
    DIRS_TO_INCLUDE = [
        "i18n"
    ]
    
    print(f"Creating plugin ZIP package: {ZIP_NAME}")
    
    # Remove existing ZIP file if it exists
    if os.path.exists(ZIP_NAME):
        os.remove(ZIP_NAME)
        print("Removed existing ZIP file")
    
    # Create ZIP file
    with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
        print("Adding files to ZIP archive...")
        
        # Add individual files
        for file_name in FILES_TO_INCLUDE:
            if os.path.exists(file_name):
                arcname = f"{plugin_folder_name}/{file_name}"
                zipf.write(file_name, arcname)
                print(f"✓ Added: {file_name}")
            else:
                print(f"✗ Not found: {file_name}")
        
        # Add directories
        for dir_name in DIRS_TO_INCLUDE:
            if os.path.exists(dir_name) and os.path.isdir(dir_name):
                for root, dirs, files in os.walk(dir_name):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = f"{plugin_folder_name}/{file_path.replace(os.sep, '/')}"
                        zipf.write(file_path, arcname)
                        print(f"✓ Added: {file_path}")
            else:
                print(f"✗ Directory not found: {dir_name}")
    
    # Get file size and show results
    if os.path.exists(ZIP_NAME):
        file_size = os.path.getsize(ZIP_NAME)
        file_size_kb = round(file_size / 1024, 2)
        
        print(f"\n✓ Successfully created: {ZIP_NAME}")
        print(f"   File size: {file_size_kb} KB")
        print(f"   Full path: {os.path.abspath(ZIP_NAME)}")
        print("\nPlugin ZIP package created successfully!")
        print("Ready for distribution or upload to QGIS Plugin Repository")
        return True
    else:
        print("✗ Error: ZIP file was not created")
        return False

def list_zip_contents(zip_name):
    """List contents of the created ZIP file for verification"""
    if not os.path.exists(zip_name):
        print(f"ZIP file {zip_name} not found")
        return
    
    print(f"\nContents of {zip_name}:")
    print("-" * 50)
    
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        for info in zipf.infolist():
            size_kb = round(info.file_size / 1024, 2) if info.file_size > 0 else 0
            print(f"{info.filename:<40} {size_kb:>8} KB")
    
    print("-" * 50)

if __name__ == "__main__":
    success = create_plugin_zip()
    
    if success:
        # Show ZIP contents for verification
        zip_name = f"QGIS_legendView_v{PLUGIN_VERSION}.zip"
        list_zip_contents(zip_name)
    else:
        exit(1)
