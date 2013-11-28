from flask import (Flask, render_template, request, make_response, request,
                   current_app, jsonify, abort, send_from_directory, redirect, Response)
from boilerflask import app


@app.route('/', methods=['GET'] )
def index():
    return render_template('index.html')
