import os
import json
import urlparse

from boilerflask.config.developmentconfig import DevelopmentConfig
from boilerflask.config.baseconfig import BaseConfig

def parseManifest(base):
    r = lambda s: s.replace(".build/","")
    rk = lambda s: s.replace(".build/static/","")
    replace_original = lambda s: s.replace("min.","")
    replace_result = lambda s : "%s/%s" % (base,s)
    loadManifest = lambda: json.loads(open("assets.json","r").read())
    return {replace_original(k): replace_result(v) for (k, v) in loadManifest().items()}

class ProductionConfig(DevelopmentConfig):
    '''
    Extends and overrides declarations from the DevelopmentConfiguration
    '''
    DEBUG = False
    MONGO_URI = os.environ.get("MONGOHQ_URL")
    ASSETS = parseManifest(BaseConfig.S3_STATIC_URL)
    CACHE_TYPE = 'simple'
    CACHE_THRESHOLD = 1000
