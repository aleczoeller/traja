# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, sys

sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "traja"
copyright = "2019, traja developers"
author = "Justin Shenk"

# The short X.Y version
import traja

version = release = traja.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx_gallery.gen_gallery",
]

# continue doc build and only print warnings/errors in examples
ipython_warning_is_error = False


doctest_global_setup = """
import pandas as pd
import traja
"""

autosummary_generate = True

# Sphinx gallery configuration
from sphinx_gallery.sorting import FileNameSortKey

sphinx_gallery_conf = {
    "examples_dirs": ["../examples"],
    #'filename_pattern': '^((?!sgskip).)*$',
    "gallery_dirs": ["gallery"],
    "doc_module": ("traja",),
    "reference_url": {
        "numpy": "http://docs.scipy.org/doc/numpy",
        "geopandas": "https://geopandas.readthedocs.io/en/latest/",
    },
    "sphinx_gallery": None,
    "backreferences_dir": "reference",
    "within_subsection_order": FileNameSortKey,
}

# Napoleon settings
napoleon_google_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "trajadoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "traja.tex", "traja Documentation", "Justin Shenk", "manual")
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "traja", "traja Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, sequence_id)
texinfo_documents = [
    (
        master_doc,
        "traja",
        "traja Documentation",
        author,
        "traja",
        "One line description of project.",
        "Miscellaneous",
    )
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org", None),
    "numpy": ("http://docs.scipy.org/doc/numpy", None),
    "matplotlib": ("http://matplotlib.sourceforge.net", None),
    "pandas": ("http://pandas-docs.github.io/pandas-docs-travis", None),
    "scipy": ("http://docs.scipy.org/doc/scipy/reference", None),
    "PyTorch": ("http://pytorch.org/docs/master/", None),
}

autodoc_member_order = "bysource"
autodoc_mock_imports = ["rpy2"]


def setup(app):
    """
    Enable documenting 'special methods' using the autodoc_ extension.
    :param app: The Sphinx application object.
    This function connects the :func:`special_methods_callback()` function to
    ``autodoc-skip-member`` events.
    .. _autodoc: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
    """
    app.connect("autodoc-skip-member", special_methods_callback)


def special_methods_callback(app, what, name, obj, skip, options):
    """
    Enable documenting 'special methods' using the autodoc_ extension.
    Refer to :func:`enable_special_methods()` to enable the use of this
    function (you probably don't want to call
    :func:`special_methods_callback()` directly).
    This function implements a callback for ``autodoc-skip-member`` events to
    include documented 'special methods' (method names with two leading and two
    trailing underscores) in your documentation. The result is similar to the
    use of the ``special-members`` flag with one big difference: Special
    methods are included but other types of members are ignored. This means
    that attributes like ``__weakref__`` will always be ignored (this was my
    main annoyance with the ``special-members`` flag).
    The parameters expected by this function are those defined for Sphinx event
    callback functions (i.e. I'm not going to document them here :-).
    """
    import types

    if getattr(obj, "__doc__", None) and isinstance(
        obj, (types.FunctionType, types.MethodType)
    ):
        return False
    else:
        return skip


# Tell sphinx what the primary language being documented is.
primary_domain = "py"

# Tell sphinx what the pygments highlight language should be.
highlight_language = "py"
