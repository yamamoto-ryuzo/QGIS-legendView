# -*- coding: utf-8 -*-
"""
Python-based translations for QGIS Legend View plugin
Fallback when .qm files are not available
"""

TRANSLATIONS = {'ja': {'LegendView': {'&凡例表示': '&凡例表示', '凡例': '凡例', 'シンボル': 'シンボル', 'その他の値': 'その他の値'}, 'LegendViewDockWidgetBase': {'凡例表示': '凡例表示', 'レイヤ名': 'レイヤ名', '不透明度': '不透明度', 'スタイル': 'スタイル'}}, 'en': {'LegendView': {'&凡例表示': '&Legend View', '凡例': 'Legend', 'シンボル': 'Symbol', 'その他の値': 'Other values'}, 'LegendViewDockWidgetBase': {'凡例表示': 'Legend View', 'レイヤ名': 'Layer Name', '不透明度': 'Opacity', 'スタイル': 'Style'}}}

def translate(context, message, locale='ja'):
    """Get translation for a message"""
    if locale in TRANSLATIONS and context in TRANSLATIONS[locale]:
        return TRANSLATIONS[locale][context].get(message, message)
    return message

def get_available_locales():
    """Return list of available locales"""
    return list(TRANSLATIONS.keys())
