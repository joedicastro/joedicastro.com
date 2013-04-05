# -*- coding: utf-8 -*-

#==============================================================================
# PELICAN SETTINGS FILE
#==============================================================================

# Add personalized 404 & 403 error pages to direct templates
DIRECT_TEMPLATES = ('index', 'tags', 'archives', 'notfound', 'access_denied')

# Default author (put your name)
AUTHOR = u'joe di castro'

# Your site name and subtitle
SITENAME = u"joe di castro"
SITESUBTITLE = u""

# If you do manage multiple languages, you can set the date formatting here.
DATE_FORMATS = {}

#Empty by default. Allows to render URLs in a particular way
ARTICLE_PERMALINK_STRUCTURE = ''

# The default category to fallback on.
#DEFAULT_CATEGORY = "blog"

#The default date format you want to use.
#DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# Display or not the pages on the menu of the template. Templates can follow or
# not this settings.
DISPLAY_PAGES_ON_MENU = True

# If True, pelican will use the file system dates infos (mtime) if it can’t get
# informations from the metadata
#FALLBACK_ON_FS_DATE = True

#A list of the extensions that the markdown processor will use.
MD_EXTENSIONS = ['codehilite', 'extra']

# A list of any Jinja2 extensions you want to use.
JINJA_EXTENSIONS = ['jinja2.ext.do']

# Delete the output directory and just the generated files. Default = False
DELETE_OUTPUT_DIRECTORY = False  # True for debugging, False for productive

# Change the locale. A list of locales can be provided here or a single string
# representing one locale. When providing a list, all the locales will be tried
# until one works.
LOCALE = ""

#The timezone used in the date information, to generate atom and rss feeds.
TIMEZONE = "Europe/Madrid"


#A list of available markup languages you want to use. For the moment, only
# available values are rst and md.
#MARKUP = ('rst', 'md')

# Where to output the generated files.
OUTPUT_PATH = 'output/'

# path to look at for input files.
PATH = "source"

# Set to True if you want to have PDF versions of your documents. You will need
# to install rst2pdf. (only for rst)
#PDF_GENERATOR = True

# Defines if pelican should use relative urls or not.
RELATIVE_URL = False

#base URL of your website. Note that this is not a way to tell pelican to use
#relative urls or static ones. You should rather use the RELATIVE_URL setting
#for such use.
SITEURL = 'http://joedicastro.com'

# The static paths you want to have accessible on the output path “static”. By
# default, pelican will copy the ‘images’ folder to the output folder.
# static paths will be copied under the same name
STATIC_PATHS = ["pictures", "ammap", ]


# Where to put the atom categories feeds.
#CATEGORY_FEED = "feeds/%s.atom.xml"

# Where to put the categories rss feeds.
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# relative url to output the atom feed.
FEED = "atom.xml"

# relative url to output the rss feed.
FEED_RSS = 'rss.xml'

# relative url to output the tags atom feed. It should be defined using a “%s”
# matchin the tag name
TAG_FEED = 'feeds/tags/%s.atom.xml'

# relative url to output the tag RSS feed
TAG_FEED_RSS = "feeds/tags/%s.rss.xml"

# Where to put the Atom feed for translations.
#TRANSLATION_FEED = "feeds/all-%s.atom.xml"

#Maximum number of items allowed in a feed. Feeds are unrestricted by default.
FEED_MAX_ITEMS = 12


# The minimum number of articles allowed on the last page. Use this when you
# don’t want to have a last page with very few articles.
DEFAULT_ORPHANS = 0

# The maximum number of articles to include on a page, not including orphans.
DEFAULT_PAGINATION = 3

#Activate pagination.
WITH_PAGINATION = True


# Count of different font sizes in the tag cloud.
TAG_CLOUD_STEPS = 4

# Maximum tags count in the cloud.
TAG_CLOUD_MAX_ITEMS = 200

# The default language to use.
DEFAULT_LANG = 'es'

# Reverse the archives order. (True makes it in descending order: the newer
# first)
REVERSE_ARCHIVE_ORDER = True
# Reverse the category order. (True makes it in descending order,
# default is alphabetically)
REVERSE_CATEGORY_ORDER = False

# theme to use to produce the output. can be the complete static path to a
# theme folder, or chosen between the list of default themes
THEME = "/home/joedicastro/code/joedicastro.com/site/joe_theme"

# Static theme paths you want to copy. Default values is static, but if
# your theme has other static paths, you can put them here.
#THEME_STATIC_PATHS = ['static']

# specify the CSS file you want to load
#CSS_FILE = 'main.css'

# Pelican can handle disqus comments, specify the sitename you’ve filled in on
# disqus
DISQUS_SITENAME = "joedicastro"

# Your github URL (if you have one), it will then use it to create a
# github ribbon.
#GITHUB_URL = 'http://github.com/joedicastro/'

#‘UA-XXXX-YYYY’ to activate google analytics.
#GOOGLE_ANALYTICS = ""

#URL to your Piwik server - without ‘http://‘ at the beginning.
PIWIK_URL = "joedicastro.com/piwik"

# If the SSL-URL differs from the normal Piwik-URL you have to include this
# setting too. (optional)
#PIWIK_SSL_URL = ""

# ID for the monitored website. You can find the ID in the Piwik admin
# nterface > settings > websites.
PIWIK_SITE_ID = "1"

# A list of tuples (Title, Url) for links to appear on the footer.
LINKS = ()

# A list of tuples (Title, Url) to appear in the “social” section.
SOCIAL = ()

# Allows to add a button on the articles to tweet about them. Add you twitter
# username if you want this button to appear.
#TWITTER_USERNAME = "joe_di_castro"


# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/humans.txt', 'humans.txt'),
                 ('extra/favicon.ico', 'favicon.ico'),
                 ('extra/apple-touch-icon.png', 'apple-touch-icon.png'),
                 ('extra/.htaccess', '.htaccess'))

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
