from flask_restplus import Resource, reqparse

from insight.util.path_finder import path_finder
from insight.service.dto import CmDto as DTO

base_data = path_finder('swagger')
DATA = base_data['impl_compare_modes']

cm_api = DTO.api
cm_model = DTO.model


@cm_api.route('')
@cm_api.param('publisher_id', 'The numerical publisher ID')
class ImplCompareModes(Resource):
    @cm_api.marshal_with(cm_model)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('publisher', type=int, location='args')
        args = parser.parse_args()
        print('args', args)

        """List all cats"""
        return DATA
