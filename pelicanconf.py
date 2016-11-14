#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Amit Visrolia'
SITENAME = 'Amit\'s notes'
SITEURL = ''
SITETITLE = 'Amit'
SITESUBTITLE = 'Notes, links, and pictures'
SITEDESCRIPTION = 'Amit\'s notes, links, and pictures'
COPYRIGHT_YEAR = 2016
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

PATH = 'content'
SLUGIFY_SOURCE = 'basename'
DEFAULT_DATE = 'fs'

THEME = 'themes/flex-amit'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

CUSTOM_CSS = 'style.local.css'

STATIC_PATHS = ['images','pdf','extra/robots.txt', 'extra/favicon.ico', 'extra/CNAME', 'extra/404.txt', 'extra/manifest.json']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/404.txt': {'path': '404.html'},
    'extra/manifest.json': {'path': 'manifest.json'},
}

FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/png'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search','render_math']

TIPUE_SEARCH_SAVE_AS = 'tipuesearch_content.json'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))
AUTHOR_SAVE_AS = ''

# Feeds
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False

# Blogroll
#LINKS = (('Google', 'https://www.google.co.uk/'),)

SOCIAL = (('xlinkedin', 'https://uk.linkedin.com/in/amitvisrolia'),
          ('github', 'https://github.com/amitviz'),
          #('google', 'https://google.com/+AmitVisrolia'),
          ('rss', '/feeds/atom.xml'))

MENUITEMS = (('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Archives', '/archives.html'),)

DEFAULT_PAGINATION = 10

TYPOGRIFY = True
