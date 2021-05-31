# FxcmAPI 福匯虛擬帳號API串接練習
import fxcmpy
import socketio

api = fxcmpy.fxcmpy(server='demo',config_file='fxcm.cfg')
api.get_account_ids()