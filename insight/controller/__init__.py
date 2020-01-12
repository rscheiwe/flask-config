from flask_restplus import Api

from .impl_short_pv import pv_api as ns3
from .impl_list_modes import lm_api as ns4
from .impl_compare_modes import cm_api as ns5

PATH = '/api/v1'

api = Api(
    title='InSight API',
    version='1.0.0',
    description='API endpoints for InSight'
)

api.add_namespace(ns3, path='{}/impl-short-pv'.format(PATH))
api.add_namespace(ns4, path='{}/impl-list-modes'.format(PATH))
api.add_namespace(ns5, path='{}/impl-compare-modes'.format(PATH))
