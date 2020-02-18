from flask_restplus import Resource, reqparse

from insight.util.path_finder import path_finder
from insight.service.dto import SdkDto as DTO

DATA = path_finder('desktop_sdk_traffic')
# DATA = base_data['impl_compare_modes']

sdk_api = DTO.api
# dt_model = DTO.model


@sdk_api.route('')
class SdkTraffic(Resource):
    # @dt_api.marshal_with(dt_model)
    def get(self):

        return DATA