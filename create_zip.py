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


def get_plugin_name_and_version_from_metadata():
    """Read plugin name and version from metadata.txt"""
    try:
        config = configparser.ConfigParser()
        config.read('metadata.txt', encoding='utf-8')
        name = config.get('general', 'name')
        version = config.get('general', 'version')
        return name, version
    except Exception as e:
        print(f"Warning: Could not read plugin name/version from metadata.txt: {e}")
        return "QGIS-legendView", "0.0.1"  # fallback

def bump_version(version_str):
    """Bump patch version (A.B.C → A.B.(C+1))"""
    parts = version_str.strip().split('.')
    if len(parts) != 3:
        return version_str  # fallback
    try:
        a, b, c = map(int, parts)
        c += 1
        return f"{a}.{b}.{c}"
    except Exception:
        return version_str

def update_metadata_version_and_changelog(new_version):
    """Update version and prepend new changelog entry to metadata.txt"""
    with open('metadata.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    changelog_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('version='):
            new_lines.append(f'version={new_version}\n')
        else:
            new_lines.append(line)
        if line.strip().startswith('changelog='):
            changelog_idx = i
    # changelog=の次の行から新バージョン履歴を挿入
    if changelog_idx is not None:
        insert_idx = changelog_idx + 1
        # 新バージョンのテンプレート履歴を挿入
        new_lines.insert(insert_idx, f'    Version {new_version}:\n    - (ここに変更内容を記載)\n')
    with open('metadata.txt', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)



def create_plugin_zip():
    """Create ZIP package for QGIS plugin distribution (auto version up)"""
    # 1. get plugin name and version
    plugin_folder_name, old_version = get_plugin_name_and_version_from_metadata()
    new_version = bump_version(old_version)
    # 2. update metadata.txt (version, changelog)
    update_metadata_version_and_changelog(new_version)
    # 3. ZIP名（QGIS-legendView-main_vX.Y.Z.zip 形式に自動対応）
    zip_name = f"{plugin_folder_name}_v{new_version}.zip"
    # 4. 必要最小限ファイル
    files_to_include = [
        "__init__.py",
        "legend_view.py",
        "legend_view_dockwidget.py",
        "legend_view_dockwidget_base.ui",
        "resources_rc.py",
        "resources_rc_qt5.py",
        "metadata.txt",
        "LICENSE",
        "README.md",
        "icon.png",
        "legend.png",
        "qt_compat.py",
        "version.py"
    ]
    dirs_to_include = ["i18n"]
    # 5. 旧バージョンZIP自動削除
    for f in os.listdir('.'):
        if f.startswith(plugin_folder_name + '_v') and f.endswith('.zip'):
            os.remove(f)
    print(f"Creating plugin ZIP package: {zip_name}")
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        print("Adding files to ZIP archive...")
        for file_name in files_to_include:
            if os.path.exists(file_name):
                arcname = f"{plugin_folder_name}/{file_name}"
                zipf.write(file_name, arcname)
                print(f"✓ Added: {file_name}")
            else:
                print(f"✗ Not found: {file_name}")
        for dir_name in dirs_to_include:
            if os.path.exists(dir_name) and os.path.isdir(dir_name):
                for root, dirs, files in os.walk(dir_name):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = f"{plugin_folder_name}/{file_path.replace(os.sep, '/')}"
                        zipf.write(file_path, arcname)
                        print(f"✓ Added: {file_path}")
            else:
                print(f"✗ Directory not found: {dir_name}")
    if os.path.exists(zip_name):
        file_size = os.path.getsize(zip_name)
        file_size_kb = round(file_size / 1024, 2)
        print(f"\n✓ Successfully created: {zip_name}")
        print(f"   File size: {file_size_kb} KB")
        print(f"   Full path: {os.path.abspath(zip_name)}")
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
