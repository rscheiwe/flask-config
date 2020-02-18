from flask_restplus import Api

from .impl_short_pv import pv_api as ns3
from .impl_long_pv import lpv_api as ns6
from .impl_list_modes import lm_api as ns4
from .impl_compare_modes import cm_api as ns5
from .impl_network_architecture import na_api as ns7

from .desktop_traffic import dt_api as ns8
from .desktop_sdk_traffic import sdk_api as ns9

PATH = '/api/v1'

api = Api(
    title='InSight API',
    version='1.0.0',
    description='API endpoints for InSight'
)

api.add_namespace(ns3, path='{}/impl-short-pv'.format(PATH))
api.add_namespace(ns6, path='{}/impl-long-pv'.format(PATH))
api.add_namespace(ns4, path='{}/impl-list-modes'.format(PATH))
api.add_namespace(ns5, path='{}/impl-compare-modes'.format(PATH))
api.add_namespace(ns7, path='{}/impl-network-architecture'.format(PATH))

api.add_namespace(ns8, path='{}/desktop-traffic'.format(PATH))
api.add_namespace(ns9, path='{}/desktop-sdk-traffic'.format(PATH))
