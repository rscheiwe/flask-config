from flask_restplus import Resource, reqparse

from insight.util.path_finder import path_finder
from insight.service.dto import LmDto as DTO

base_data = path_finder('swagger')
DATA = base_data['impl_list_modes']

lm_api = DTO.api
lm_model = DTO.model


@lm_api.route('')
@lm_api.param('publisher_id', 'The numerical publisher ID')
class ImplListModes(Resource):
    @lm_api.marshal_with(lm_model)
    @lm_api.response(400, 'Bad Request -- Publisher required')
    @lm_api.response(502, 'Bad Gateway -- Check server')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('publisher', type=int, location='args')
        args = parser.parse_args()
        print('args', args)

        """List all cats"""
        return DATA