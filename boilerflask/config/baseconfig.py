#
# @author Cory Dolphin
# @wcdolphin
#
import urlparse

class BaseConfig(object):
    """
    Basic default global configuration variables not specific to any environment
    """
    DEBUG = True
    SECRET_KEY = 'supersecret'
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''
    MONGODB_HOST  = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_DB = 'demo'
    S3_STATIC_URL = "//" #fix this 