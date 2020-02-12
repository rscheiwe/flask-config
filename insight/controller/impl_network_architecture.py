import os
from flask_restplus import Resource, reqparse

from insight.util.json_read_write import load_json
from insight.service.dto import NaDto as DTO

abs_path = os.path.abspath('.')
path_to_file = os.path.join(abs_path, "config/_swagger.json")
swagger_data = load_json(path_to_file)

DATA = swagger_data['impl_network_architecture']

na_api = DTO.api
na_model = DTO.model


@na_api.route('')
@na_api.param('network_id', 'The numerical network ID')
class ImplLongPV(Resource):
    @na_api.marshal_with(na_model)
    @na_api.response(400, 'Bad Request -- Publisher required')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('network', type=int, location='args')
        args = parser.parse_args()
        print('args', args)

        return DATA