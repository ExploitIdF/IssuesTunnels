project = 'Issues de secours'
copyright = '2024-02, on'
author = 'on'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_css_files = ['custom.css']
html_favicon = 'https://storage.googleapis.com/ref-dett/faviconIssues.png'
html_static_path = ['_static']
html_show_copyright = False
html_show_sphinx = False
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logoIssuesSec.jpg",
    "dark_logo": "logoIssuesSec.jpg",   
}
