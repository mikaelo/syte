
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'aventuristo.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'dc2VOYTyK4GAhuRQooiZmwIccVUM0EpuQKCXq1p3L5ckAHLLgm'


#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&screen_name='
TWITTER_CONSUMER_KEY = 'l9DJryQSKXcgCEIOk6vjAw'
TWITTER_CONSUMER_SECRET = 'YJw3EhluG54LW9exdjjiZIDpAADDTkiuHg91r3wnYY'
TWITTER_USER_KEY = '19621689-C7YiDIUyjnKZoFldaE2gOAdj2beGvZiQ29EkjqZoE'
TWITTER_USER_SECRET = 'cFsKDiPCEvCAGhP8ANj7IyLr70nSS2S8KwwIlKYgc'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '2156e09993f16f4113a0de9bdb64adfa93afe2cf'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = '12d8b4b5d4ef65f8ff9f'
GITHUB_CLIENT_SECRET = 'f24b5033ccc951ab54a278f4686ed3defbaf543d'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = True
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '1411538.85ef042.0625d6a1484b4da2907a93c5d76d8d21'
INSTAGRAM_USER_ID = '1411538'

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = '85ef042e9cdd428b9c5ecf9b117f265c'
INSTAGRAM_CLIENT_SECRET = '505982846b9b4a51b985b85d55f28a48'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://mikaelo.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
