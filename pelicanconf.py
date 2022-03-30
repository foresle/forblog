AUTHOR = 'foresle'
SITENAME = 'forblog'
SITEURL = 'http://forblog.live'

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'uk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My Matrix server', 'https://opulus.space/'),)

# Social widget
#SOCIAL = (('GitHub', 'https://github.com/foresle'),
#          ('Matrix', 'https://matrix.to/#/@foresle:matrix.opulus.space'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Pelican Alchemy theme settings

THEME = "pelican-alchemy/alchemy"
HIDE_AUTHORS = True
PYGMENTS_STYLE = 'monokai'
ICONS = (
    ('github', 'https://github.com/nairobilug/pelican-alchemy'),
    ('hashtag', 'https://matrix.to/#/@foresle:matrix.opulus.space'),
    ('mastodont', 'https://social.net.ua/foresle')
)
SITESUBTITLE = 'foresle blog'
SITEIMAGE = '/images/mr-robot_red-wheelbarrow_looney-esmail.jpg'
DESCRIPTION = 'Just another blog.'
THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']
