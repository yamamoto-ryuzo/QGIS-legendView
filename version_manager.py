#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Version Management Script for QGIS Legend View Plugin
Handles version updates, metadata synchronization, and release management
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

def read_version():
    """Read current version from version.py"""
    try:
        with open('version.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        major = re.search(r'MAJOR = (\d+)', content).group(1)
        minor = re.search(r'MINOR = (\d+)', content).group(1)
        patch = re.search(r'PATCH = (\d+)', content).group(1)
        
        prerelease_match = re.search(r'PRERELEASE = "([^"]*)"', content)
        prerelease = prerelease_match.group(1) if prerelease_match else ""
        
        return {
            'major': int(major),
            'minor': int(minor),
            'patch': int(patch),
            'prerelease': prerelease
        }
    except Exception as e:
        print(f"Error reading version: {e}")
        return None

def write_version(major, minor, patch, prerelease=""):
    """Write new version to version.py"""
    try:
        content = f'''# -*- coding: utf-8 -*-
"""
Version information for QGIS Legend View plugin
"""

# Version components
MAJOR = {major}
MINOR = {minor}
PATCH = {patch}

# Pre-release identifier (alpha, beta, rc) - empty for stable releases
PRERELEASE = "{prerelease}"

# Build metadata
BUILD = ""

def get_version():
    """Get the full version string"""
    version = f"{{MAJOR}}.{{MINOR}}.{{PATCH}}"
    
    if PRERELEASE:
        version += f"-{{PRERELEASE}}"
    
    if BUILD:
        version += f"+{{BUILD}}"
    
    return version

def get_version_info():
    """Get version information as a dictionary"""
    return {{
        'major': MAJOR,
        'minor': MINOR,
        'patch': PATCH,
        'prerelease': PRERELEASE,
        'build': BUILD,
        'version': get_version()
    }}

def is_stable():
    """Check if this is a stable release"""
    return not PRERELEASE

def get_compatibility_info():
    """Get QGIS compatibility information"""
    return {{
        'minimum_qgis_version': '3.0',
        'maximum_qgis_version': '3.99',
        'qt5_support': True,
        'qt6_support': True,
        'supported_qgis_versions': ['3.0', '3.4', '3.10', '3.16', '3.22', '3.28', '3.30+']
    }}

# Version string for easy import
__version__ = get_version()

if __name__ == "__main__":
    print(f"QGIS Legend View Plugin Version: {{get_version()}}")
    print(f"Version Info: {{get_version_info()}}")
    print(f"Is Stable: {{is_stable()}}")
    print(f"Compatibility: {{get_compatibility_info()}}")'''
        
        with open('version.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error writing version: {e}")
        return False

def update_metadata_version(version_string):
    """Update version in metadata.txt"""
    try:
        with open('metadata.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update version line
        content = re.sub(r'version=.*', f'version={version_string}', content)
        
        with open('metadata.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated metadata.txt version to {version_string}")
        return True
    except Exception as e:
        print(f"Error updating metadata.txt: {e}")
        return False

def bump_version(component, prerelease=""):
    """Bump version component"""
    version = read_version()
    if not version:
        return False
    
    if component == 'major':
        version['major'] += 1
        version['minor'] = 0
        version['patch'] = 0
    elif component == 'minor':
        version['minor'] += 1
        version['patch'] = 0
    elif component == 'patch':
        version['patch'] += 1
    
    version['prerelease'] = prerelease
    
    # Write new version
    if write_version(version['major'], version['minor'], version['patch'], prerelease):
        version_string = f"{version['major']}.{version['minor']}.{version['patch']}"
        if prerelease:
            version_string += f"-{prerelease}"
        
        # Update metadata.txt
        update_metadata_version(version_string)
        
        print(f"Version bumped to {version_string}")
        return True
    
    return False

def show_current_version():
    """Display current version information"""
    version = read_version()
    if version:
        version_string = f"{version['major']}.{version['minor']}.{version['patch']}"
        if version['prerelease']:
            version_string += f"-{version['prerelease']}"
        
        print(f"Current version: {version_string}")
        print(f"  Major: {version['major']}")
        print(f"  Minor: {version['minor']}")
        print(f"  Patch: {version['patch']}")
        if version['prerelease']:
            print(f"  Pre-release: {version['prerelease']}")
    else:
        print("Could not read version information")

def main():
    """Main version management function"""
    if len(sys.argv) < 2:
        print("QGIS Legend View Plugin - Version Management")
        print("\nUsage:")
        print("  python version_manager.py show           - Show current version")
        print("  python version_manager.py major          - Bump major version")
        print("  python version_manager.py minor          - Bump minor version") 
        print("  python version_manager.py patch          - Bump patch version")
        print("  python version_manager.py alpha          - Set as alpha release")
        print("  python version_manager.py beta           - Set as beta release")
        print("  python version_manager.py rc             - Set as release candidate")
        print("  python version_manager.py stable         - Mark as stable release")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'show':
        show_current_version()
    elif command in ['major', 'minor', 'patch']:
        bump_version(command)
    elif command in ['alpha', 'beta', 'rc']:
        version = read_version()
        if version:
            write_version(version['major'], version['minor'], version['patch'], command)
            version_string = f"{version['major']}.{version['minor']}.{version['patch']}-{command}"
            update_metadata_version(version_string)
            print(f"Version set to {version_string}")
    elif command == 'stable':
        version = read_version()
        if version:
            write_version(version['major'], version['minor'], version['patch'], "")
            version_string = f"{version['major']}.{version['minor']}.{version['patch']}"
            update_metadata_version(version_string)
            print(f"Version set to stable: {version_string}")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
