# Arquivo de configuração para o construtor de documentação Sphinx.
#
# Este arquivo contém apenas uma seleção das opções mais comuns. Por um completo
# lista veja a documentação:
# http://www.sphinx-doc.org/en/master/config

# -- Configuração de caminho --------------------------------------------------------------

# Se as extensões (ou módulos para documentar com autodoc) estiverem em outro diretório, 
# adicione esses diretórios a sys.path aqui. Se o diretório for relativo à raiz da documentação, 
# use os.path.abspath para torná-lo absoluto, como mostrado aqui.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
version = '1.0.1'

source_suffix = '.rst'
master_doc = 'index'

html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('overrides.css')  # também pode ser um URL

html_context = {
	"display_github": False, # Adicione o link Editar no Github 'em vez de' Ver o código-fonte da página
	"last_updated": True,
	"commit": False,
     }

# -- Informações do Projeto -----------------------------------------------------

project = 'Download de imagens do Google'
copyright = 'Github'
author = 'Github'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bizstyle'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'searchbox.html'] }

