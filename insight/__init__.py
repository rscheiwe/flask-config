import os
from flask import Flask
from insight.controller import api
from flask_cors import CORS
from flask_restplus import Api

from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[config_name])
    # app.url_map.strict_slashes = False
    api.init_app(app)

    return app


# app = Flask(__name__)

app = create_app(os.getenv('BOILERTPLATE_ENV') or 'dev')


# from insight.controller import routes


