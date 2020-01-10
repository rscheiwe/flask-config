from flask_restplus import Api

from .routes import api as ns1
from .routes1 import api as ns2

api = Api(
    title = 'My Tittle',
    version = '1.0',
    description = 'A descriptions'
)

api.add_namespace(ns1)
api.add_namespace(ns2)