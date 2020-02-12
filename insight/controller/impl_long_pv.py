import os
from flask_restplus import Resource, reqparse

from insight.util.json_read_write import load_json
from insight.service.dto import LpvDto as DTO

abs_path = os.path.abspath('.')
path_to_file = os.path.join(abs_path, "config/_swagger.json")
swagger_data = load_json(path_to_file)

DATA = swagger_data['impl_long_pv']

lpv_api = DTO.api
lpv_model = DTO.model


@lpv_api.route('')
@lpv_api.param('publisher_id', 'The numerical publisher ID')
class ImplLongPV(Resource):
    @lpv_api.marshal_with(lpv_model)
    @lpv_api.response(400, 'Bad Request -- Publisher required')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('publisher', type=int, location='args')
        args = parser.parse_args()
        print('args', args)

        return DATA
