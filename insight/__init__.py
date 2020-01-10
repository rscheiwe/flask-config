from flask import Flask

app = Flask(__name__)

from insight.controller import routes