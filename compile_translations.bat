# QM file compilation script
# This script compiles .ts files to .qm files for use in QGIS
# Run this script when you update translations

# To compile Japanese translation
lrelease i18n/LegendView_ja.ts

# To compile English translation
lrelease i18n/LegendView_en.ts

echo "Translation files compiled successfully"
