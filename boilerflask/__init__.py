#
# @author Cory Dolphin
# @wcdolphin
#
import os
from flask import Flask, render_template, request, redirect, url_for, abort
from urlparse import urlparse
from boilerflask import config #our super sweet configuration module!



static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.build')
print static_dir

app = Flask(__name__, static_folder=static_dir	)

app.configType = config.getConfig() #Are we running locally, in production? In Testing? This object will manage configuration!
app.config.from_object(app.configType)

print "Running using %s " % app.configType

## Register utility functions for use in views.
from boilerflask import utils
app.jinja_env.globals['static'] = utils.static_url

## Register views
from boilerflask import views