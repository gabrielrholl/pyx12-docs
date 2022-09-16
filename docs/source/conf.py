# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

import sphinx_rtd_theme
import pyx12

# -- Project information

project = 'Pyx12'
#copyright = '2022, Gabriel Rholl'
copyright = '2022, Documentation by Gabriel Rholl. ' + \
            'Pyx12 is written and maintained by John Holland, with ' + \
            'all rights reserved. (https://github.com/azoner/pyx12)'
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
