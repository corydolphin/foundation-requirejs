import os
from flask import Flask, render_template, request, redirect, url_for, abort
from urlparse import urlparse
from boilerflask import config #our super sweet configuration module!

# Tell flask our custom static directory's location
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.build')
app = Flask(__name__, static_folder=static_dir	)


#Are we running locally, in production? In Testing? This object will manage configuration!
app.configType = config.getConfig()
app.config.from_object(app.configType)

print "Running using %s " % app.configType

## Register utility functions for use in views.
from boilerflask import utils
app.jinja_env.globals['static'] = utils.static_url

## Register views
from boilerflask import views