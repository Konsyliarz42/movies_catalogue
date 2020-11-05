from flask import Flask, render_template, request
import os

patch   = os.path.join(os.path.abspath(__file__),'../instance')
app     = Flask(__name__, instance_relative_config=True, instance_path=patch)

app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)
API_KEY = app.config['API_KEY']

from . import routes