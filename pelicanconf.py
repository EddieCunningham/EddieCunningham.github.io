AUTHOR = 'Eddie Cunningham'
SITENAME = ''
SITEURL = ''

STATIC_PATHS = ['generax', 'static', 'images']
PAGE_EXCLUDES = ['generax']
ARTICLE_EXCLUDES = ['generax', 'papers', 'projects']
THEME_TEMPLATES_OVERRIDES = ['templates', 'generax']

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
PAGE_PATHS = ['pages']

PATH = 'content'

# Limit articles to a dedicated folder to avoid processing root-level notes
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# CONTACTS = (('twitter', 'https://twitter.com/_ecunningham_'),)

TWITTER_ADDRESS = 'https://twitter.com/_ecunningham_'
GITHUB_ADDRESS = 'https://github.com/EddieCunningham'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/flex"

# Custom assets and favicon
CUSTOM_CSS = 'static/custom.css'
FAVICON = '/static/favicon.svg'

# Ensure Markdown files are parsed
MARKUP = ('md', 'rst')

# Configure Markdown to read front-matter metadata
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.meta': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {'permalink': False},
    },
    'output_format': 'html5',
}
