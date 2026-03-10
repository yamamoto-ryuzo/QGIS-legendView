### 今後は　GeoReport　へ統合予定

# QGIS-legendView  
　This repository is intended to build a better QGIS environment and to provide mutual assistance among engineers by the shortage engineers by releasing additional functions of QGIS created by the open source ordered by Soja City and by having as many people as possible contribute programs to extend the functions.  
　このリポジトリは総社市が発注したオープンソースにより作成されたQGISの追加機能を公開し、多くのユーザーに利用してもらうことで、 機能拡張プログラムの提供をしていただく ことで、よりよいQGIS環境を構築するとともに、不足技術者による技術者間の互助を目的としています。

　初期バージョンの開発業者：オービタルネット　https://www.orbitalnet.jp/

## Internationalization / 国際化対応

This plugin supports multiple languages:
- English (en)
- Japanese (ja)

The interface will automatically display in your system's language if supported, otherwise it will fall back to English.

このプラグインは複数の言語に対応しています：
- 英語（en）  
- 日本語（ja）

システムの言語設定に基づいて自動的に対応言語で表示され、対応していない言語の場合は英語が使用されます。

## Qt Compatibility / Qt互換性

This plugin is compatible with both Qt5 and Qt6:
- **Qt5 Support**: QGIS 3.0 to 3.21 (PyQt5)
- **Qt6 Support**: QGIS 3.22+ (PyQt6)

The plugin automatically detects the Qt version and imports the appropriate modules. This ensures compatibility across different QGIS versions.

このプラグインはQt5とQt6の両方に対応しています：
- **Qt5サポート**: QGIS 3.0～3.21（PyQt5）
- **Qt6サポート**: QGIS 3.22以降（PyQt6）

プラグインはQtバージョンを自動検出し、適切なモジュールをインポートします。これにより、異なるQGISバージョン間での互換性を確保しています。

## Version Management / バージョン管理

This plugin includes a comprehensive version management system:

### Current Version: 2.0.0

### Version Management Tools:
- `version.py` - Centralized version information
- `version_manager.py` - Version management script
- `CHANGELOG.md` - Detailed change log

### Usage Examples:
```bash
# Show current version
python version_manager.py show

# Bump version numbers
python version_manager.py major    # 2.0.0 -> 3.0.0
python version_manager.py minor    # 2.0.0 -> 2.1.0  
python version_manager.py patch    # 2.0.0 -> 2.0.1

# Set pre-release versions
python version_manager.py alpha    # 2.0.0-alpha
python version_manager.py beta     # 2.0.0-beta
python version_manager.py rc       # 2.0.0-rc
python version_manager.py stable   # 2.0.0 (remove pre-release)
```

バージョン管理システム:
- セマンティックバージョニング（Semantic Versioning）に準拠
- 自動的にmetadata.txtと同期
- CHANGELOGによる変更履歴管理
- プリリリース版とビルドメタデータのサポート

### usage rules/利用方法
　Simply set the project variable legend_group_name_layer_name and specify the order of display as 1,2,3,・・・・.  
　プロジェクト変数に　legend_グループ名_レイヤ名 を設定し，表示する順番を　1,2,3,････　と指定するだけです。  

#### Setting Example/設定例
![image](https://user-images.githubusercontent.com/86514652/209086882-101a082b-6325-4ebb-9a85-3b9086f01c2b.png)
![image](https://user-images.githubusercontent.com/86514652/209077526-44c264dd-4377-461f-9940-5cfe5a7100bc.png)

#### Display example/表示例
![image](https://user-images.githubusercontent.com/86514652/209077323-d3b375f9-b713-4ca6-8388-1b82c24b6d50.png)
<img width="363" height="378" alt="image" src="https://github.com/user-attachments/assets/b3635409-68ef-496b-967e-28f6987e556c" />

