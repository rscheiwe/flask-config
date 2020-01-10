# from insight import app
from flask_restplus import Namespace, Resource, fields

# api = Api(app)
api = Namespace('dogs', description='Dogs related operations')
dog = api.model('Dog', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

DOGS = [
    {'id': 'henry', 'name': 'henry'},
]
# from insight.util.dto import MainDto


@api.route('/')
class DogList(Resource):
    @api.doc(responses={200: """['s1', 's2', 's3']"""})
    @api.marshal_list_with(dog)
    def get(self):
        """List all cats"""
        return DOGS