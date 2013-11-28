#
# @author Cory Dolphin
# @wcdolphin
#
from boilerflask.config.baseconfig import BaseConfig

class DevelopmentConfig(BaseConfig):
    """
    The Development Configuration, provides default database and facebook credentials and
    configuration to run the application
    """
    CACHE_TYPE = 'null'
