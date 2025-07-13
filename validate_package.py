#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QGIS Plugin Package Validator
Validates plugin packages for QGIS Plugin Repository requirements
"""

import os
import zipfile
import configparser
from pathlib import Path

def validate_plugin_package(zip_path):
    """Validate a QGIS plugin ZIP package"""
    
    print(f"Validating plugin package: {zip_path}")
    print("=" * 50)
    
    if not os.path.exists(zip_path):
        print("❌ ZIP file not found")
        return False
    
    errors = []
    warnings = []
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            file_list = zipf.namelist()
            
            # Extract plugin name from first directory
            plugin_name = file_list[0].split('/')[0] if file_list else None
            if not plugin_name:
                errors.append("Cannot determine plugin name from ZIP structure")
                return False
            
            print(f"Plugin name: {plugin_name}")
            print(f"Total files: {len(file_list)}")
            print()
            
            # Required files check
            required_files = [
                '__init__.py',
                'metadata.txt',
                'LICENSE'
            ]
            
            print("Required files check:")
            for req_file in required_files:
                full_path = f"{plugin_name}/{req_file}"
                if full_path in file_list:
                    print(f"✅ {req_file}")
                else:
                    errors.append(f"Missing required file: {req_file}")
                    print(f"❌ {req_file}")
            
            print()
            
            # Recommended files check
            recommended_files = [
                'README.md',
                'CHANGELOG.md',
                'icon.png'
            ]
            
            print("Recommended files check:")
            for rec_file in recommended_files:
                full_path = f"{plugin_name}/{rec_file}"
                if full_path in file_list:
                    print(f"✅ {rec_file}")
                else:
                    warnings.append(f"Missing recommended file: {rec_file}")
                    print(f"⚠️  {rec_file}")
            
            print()
            
            # Validate metadata.txt
            metadata_path = f"{plugin_name}/metadata.txt"
            if metadata_path in file_list:
                print("Metadata validation:")
                try:
                    metadata_content = zipf.read(metadata_path).decode('utf-8')
                    config = configparser.ConfigParser()
                    config.read_string(metadata_content)
                    
                    required_metadata = [
                        ('general', 'name'),
                        ('general', 'version'),
                        ('general', 'qgisMinimumVersion'),
                        ('general', 'description'),
                        ('general', 'author'),
                        ('general', 'email')
                    ]
                    
                    for section, key in required_metadata:
                        if config.has_option(section, key):
                            value = config.get(section, key)
                            print(f"✅ {key}: {value}")
                        else:
                            errors.append(f"Missing metadata: [{section}] {key}")
                            print(f"❌ {key}: Missing")
                    
                except Exception as e:
                    errors.append(f"Error reading metadata.txt: {e}")
                    print(f"❌ Error reading metadata.txt: {e}")
            
            print()
            
            # Check for Python files
            python_files = [f for f in file_list if f.endswith('.py')]
            print(f"Python files found: {len(python_files)}")
            
            # Check for UI files
            ui_files = [f for f in file_list if f.endswith('.ui')]
            if ui_files:
                print(f"UI files found: {len(ui_files)}")
            
            # Check for translation files
            translation_files = [f for f in file_list if f.endswith('.qm') or f.endswith('.ts')]
            if translation_files:
                print(f"Translation files found: {len(translation_files)}")
            
            # Check for resource files
            resource_files = [f for f in file_list if f.endswith('.qrc') or f.endswith('_rc.py')]
            if resource_files:
                print(f"Resource files found: {len(resource_files)}")
            
    except zipfile.BadZipFile:
        errors.append("Invalid ZIP file format")
        print("❌ Invalid ZIP file format")
    except Exception as e:
        errors.append(f"Unexpected error: {e}")
        print(f"❌ Unexpected error: {e}")
    
    print()
    print("Validation Summary:")
    print("=" * 50)
    
    if errors:
        print("❌ ERRORS:")
        for error in errors:
            print(f"   • {error}")
        print()
    
    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   • {warning}")
        print()
    
    if not errors and not warnings:
        print("✅ Package validation passed with no issues!")
    elif not errors:
        print("✅ Package validation passed with warnings")
    else:
        print("❌ Package validation failed")
    
    return len(errors) == 0

def main():
    """Main validation function"""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python validate_package.py <plugin_zip_file>")
        return
    
    zip_path = sys.argv[1]
    success = validate_plugin_package(zip_path)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
