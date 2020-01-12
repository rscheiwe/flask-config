import os
from flask_restplus import Resource, reqparse

from insight.util.json_read_write import load_json
from insight.service.dto import CmDto as DTO

abs_path = os.path.abspath('.')
path_to_file = os.path.join(abs_path, "config/_swagger.json")
swagger_data = load_json(path_to_file)

DATA = swagger_data['impl_compare_modes']

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
