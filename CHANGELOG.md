# Changelog

All notable changes to the QGIS Legend View plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).



## [2.0.2] - 2025-07-20

### Changed
- Currentボタンの幅を1.5倍に拡大
- legend_view_dockwidget_base.uiのUI調整
- 各言語翻訳ファイルの構造修正・再生成（.ts/.qm）
- ドイツ語・イタリア語翻訳ファイルの再構築
- lreleaseによる全言語の.qm再生成
- 最新の翻訳・UI修正を反映したZIPパッケージ作成

### Fixed
- 多言語翻訳抽出・反映の不具合修正
- .tsファイルの重複・壊れたXML宣言の整理
- Currentボタンの翻訳が抽出されない問題の修正

### Added
- CHANGELOG.mdのバージョン管理手順明記
- バージョン管理スクリプトの利用例をREADME等に追記

---

## [Unreleased]

## [2.0.1] - 2025-07-13

### Fixed
- Added missing LICENSE file to plugin package
- Added README.md to plugin package for better documentation
- Enhanced ZIP package validation system

### Added
- Plugin package validator script (validate_package.py)
- Comprehensive package validation with error reporting
- Improved packaging system with all required files

## [2.0.0] - 2025-07-13

### Added
- Qt5/Qt6 compatibility support
- Multi-language support (Japanese and English)
- Python-based translation fallback system
- Automatic Qt version detection
- Comprehensive version management system
- Improved error handling and robustness

### Changed
- Default interface language changed to Japanese
- Enhanced translation system with fallback mechanisms
- Improved compatibility across QGIS versions (3.0 to 3.30+)
- Updated plugin architecture for better maintainability

### Technical Improvements
- Added `qt_compat.py` for Qt version compatibility
- Implemented `version.py` for centralized version management
- Added `translations.py` for Python-based translation fallback
- Enhanced ZIP packaging system with version awareness

### Fixed
- Translation issues in Japanese interface
- Qt version compatibility problems
- Plugin loading errors in different QGIS versions

## [1.0.0] - 2020-10-28

### Added
- Initial release
- Basic legend display functionality
- Dockable widget interface
- Project variable-based layer selection
- Support for vector and raster layers
- Opacity control
- Named style support

### Features
- Display selected layer legends in a compact widget
- Configure display order using project variables
- Support for various layer types and symbology
- Integration with QGIS layer tree

---

## Version Format

This project uses [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backward-compatible functionality additions  
- **PATCH** version for backward-compatible bug fixes

Additional labels for pre-release and build metadata:
- **alpha**, **beta**, **rc** for pre-release versions
- **build** metadata for development builds
