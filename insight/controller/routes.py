# from insight import app
from flask_restplus import Namespace, Resource, fields

# api = Api(app)
api = Namespace('cats', description='Cats related operations')
cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]
# from insight.util.dto import MainDto


@api.route('/')
class CatList(Resource):
    @api.doc(responses={200: """['s1', 's2', 's3']"""})
    @api.marshal_list_with(cat)
    def get(self):
        """List all cats"""
        return CATS


# @api.route('/cats')
# class CatJson(Resource):
#     def catJson(self):
#         return CATS

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
