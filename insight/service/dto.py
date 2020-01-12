from flask_restplus import Namespace, fields


class PvDto:
    api = Namespace('impl-short-pv', description='Short PV Analysis for Publisher')
    nested_pv_data = api.model(
        'pv_by_mode', {
            'MODE': fields.String,
            'num_views': fields.Integer,
            'publisher_id': fields.Integer,
            'rolling_mean': fields.Integer
        })
    pv_data = api.model(
        'pv_data', {
            'daterange': fields.String,
            'json_response': fields.List(fields.Nested(nested_pv_data))
    })
    model = api.model(
        'pv_final', {
            'data': fields.List(fields.Nested(pv_data))
    })

# class PvDto():
#
#     def __init__(self):
#         self.api = Namespace('impl-short-pv', description='Short PV Analysis for Publisher')
#         self.modemodel = self.api.model(
#             'pv_by_mode', {
#                 'MODE': fields.String,
#                 'num_views': fields.Integer,
#                 'publisher_id': fields.Integer,
#                 'rolling_mean': fields.Integer
#             })
#         self.pv_data = self.api.model(
#             'pv_data', {
#                 'daterange': fields.String,
#                 'json_response': fields.List(fields.Nested(self.modemodel))
#         })
#         self.model = self.api.model(
#             'ImplShortPv', {
#                 'data': fields.List(fields.Nested(self.pv_data))
#         })





class LmDto:
    api = Namespace('impl-list-modes', description='List Modes in Publisher-level Loader')
    nested_core_data = api.model(
        'lm_by_mode', {
            'MODE': fields.String,
            'archived': fields.String,
            'mode_date': fields.String,
            'mode_id': fields.Integer
        })
    nested_data = api.model(
        'lm_data', {
            'json_response': fields.List(fields.Nested(nested_core_data))
    })
    model = api.model(
        'lm_final', {
            'data': fields.List(fields.Nested(nested_data))
    })


class CmDto:
    api = Namespace('impl-compare-modes', description='Compare Modes at Publisher Level')
    nested_cm_data = api.model(
        'cm_by_mode', {
            'MODE_NAMES': fields.String,
            'MODE_TYPE': fields.String,
            'count': fields.Integer,
            'number_views': fields.Integer,
            'publisher_id': fields.Integer
        })
    cm_data = api.model(
        'cm_data', {
            'active_modes': fields.List(fields.String),
            'all_modes': fields.List(fields.Nested(nested_cm_data)),
            'daterange': fields.String,
            'inactive_modes': fields.List(fields.String)
        })
    model = api.model(
        'cm_final', {
            'data': fields.List(fields.Nested(cm_data))
        }
    )