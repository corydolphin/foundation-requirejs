import os
import json
import urlparse
import sys

def getConfig():
    ''' Should return the proper configuration based upon environmental
        variables and or other subsequent tests. Currently only distinguishes
        between Heroku and 'other', defaulting other to a local development database.
        TODO: test for local development database, if failed, default to a remote
        database, there should be no need for a full postgres install to test
        or write client/HTML/CSS/js.
    '''
    if os.environ.get('PYTHONHOME') != None and 'heroku' in os.environ.get('PYTHONHOME'): ##we are on Heroku!
        from boilerflask.config.productionconfig import ProductionConfig
        return ProductionConfig
    else:
        from boilerflask.config.developmentconfig import DevelopmentConfig
        return DevelopmentConfig

if __name__ == '__main__':
    print getConfig()
