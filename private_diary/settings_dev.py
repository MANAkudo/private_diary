from.settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ou@l(#ko9)ry#jxax43)ep(cen=m8v4p6=b3a&a!8wv=x4^ln1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    'version': 1, #1固定
    'disable_existing_loggers': False,

#ロガーの設定
'loggers':{
#    Diangoが利用するロガー
    'django':{
        'handlers':['console'],
        'level':'INFO',
    },
    #diaryアプリケーションが利用するロガー
    'diary':{
        'handlers':['console'],
        'level':'DEBUG',
    },
  },
#     ハンドラの設定
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },
    # フォーマッタの設定
    'formatters':{
        'dev':{
            'format':'\t'.join([
            '[%(levelname)s]',
            '%(pathname)s(Line:%(lineno)d)',
            '%(message)s'
          ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')




