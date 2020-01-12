import os
import json
from flask import jsonify
from flask_restplus import Resource, reqparse, marshal, fields

from insight.util.json_read_write import load_json
from insight.service.dto import PvDto as DTO

abs_path = os.path.abspath('.')
path_to_file = os.path.join(abs_path, "config/_swagger.json")
swagger_data = load_json(path_to_file)

DATA = swagger_data['impl_short_pv']

pv_api = DTO().api
pv_model = DTO().model

# pv_api = DTO.api
# pv_model = DTO.model

my_resource_parser = reqparse.RequestParser()
my_resource_parser.add_argument('publisher', type=int, default='string: name', required=True)

@pv_api.route('')
# @pv_api.param('publisher_id', 'The numerical publisher ID')
class ImplShortPv(Resource):
    @pv_api.marshal_with(pv_model)
    @pv_api.response(400, 'Bad Request -- Publisher required')
    @pv_api.expect(my_resource_parser)
    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('publisher', type=int, location='args')
        args = my_resource_parser.parse_args()
        print('args', args)

        """List all cats"""
        return DATA



# @pv_api.route('')
# @pv_api.param('publisher_id', 'The numerical publisher ID')
# class ImplShortPv(Resource):
#     @pv_api.marshal_with(pv_model)
#
#     # @pv_api.responlist_se(200, 'Success', pv_model)
#     @pv_api.response(400, 'Bad Request -- Publisher required')
#     def get(self):
#         print(pv_model)
#         return DATA
