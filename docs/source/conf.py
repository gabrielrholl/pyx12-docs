# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

import sphinx_rtd_theme
import pyx12

# -- Project information

project = 'Pyx12'
copyright = '2022, Gabriel Rholl'
author = 'Gabriel Rholl'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'pyx12',
]

# Autodoc settings
autodoc_default_options = {
    'members': True
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_theme_path = ["sphinx_rtd_theme", ]

# -- Options for EPUB output
epub_show_urls = 'footnote'
