#
# @author Cory Dolphin
# @wcdolphin
#
from boilerflask import app
from flask import url_for
def static_url(filename):
    if "ASSETS" in app.config:
        return app.config["ASSETS"][filename]
    else:
        return url_for("static", filename=filename)