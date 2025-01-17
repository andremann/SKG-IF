# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'SKG-IF'
copyright = '2024, RDA SKG-IF WG, Andrea Mannocci, Miriam Baglioni'
author = 'RDA SKG-IF WG, Andrea Mannocci, Miriam Baglioni'

release = 'discontinued'
version = 'discontinued'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_extra_path = ['./robots.txt', './google61890b13e02c7380.html']