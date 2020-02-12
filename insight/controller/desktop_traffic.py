from flask_restplus import Resource, reqparse

from insight.util.path_finder import path_finder
from insight.service.dto import DtDto as DTO

DATA = path_finder('desktop_traffic')
# DATA = base_data['impl_compare_modes']

dt_api = DTO.api
# dt_model = DTO.model


@dt_api.route('')
class DesktopTraffic(Resource):
    # @dt_api.marshal_with(dt_model)
    def get(self):

        return DATA