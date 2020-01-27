#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
# sys.path.insert(0, os.path.abspath('../../dallasparser'))
sys.path.append(os.path.abspath('../../dallasparser'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'TX Dallas Criminal Court Case Parser'
copyright = '2020, Jay C.'
author = 'Jay C.'

# The full version, including alpha/beta/rc tags
version = '0.3'
release = '0.3'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# If true, `todo` and `todoList` produces output, else they produce nothing.
todo_include_todos = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Output file base name for HTML help builder
htmlhelp_basename = 'TXDallasParserDoc'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
    'papersize':'a4paper',
    'pointsize':'10pt',
    'extraclassoptions':'openany,onesisde',
    'tableofcontents':'',
    'printindex':'\\footnotesize\\raggedright\\printindex',
}
latex_documents = [
    (master_doc, 'txdallasparser.tex', 'TX Dallas Parser Documentation',
        author, 'manual')
]

# -- Options for Texinfo output -------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
# dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'TXDallasParser', 'TX Dallas Parser Documentation',
    author, 'TXDallasParser', 'One line description of project.',
    'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------
# Bibliographic Dublic Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']
