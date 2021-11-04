import datetime
from threading import current_thread
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

app = Flask()
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


@app.route('/refresh', method=['POST'])
# @jwt_refresh_token_required # @jwt_refresh_token_required 就是現在 @jwt_required(refresh=True)
# https://flask-jwt-extended.readthedocs.io/en/stable/v4_upgrade_guide/?highlight=jwt_refresh_token_required#api-changes
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200

# JWT Token 過期時間預設為 15 分鐘，Refresh Token 過期時間預設為 30 天，可以依照自己喜好修改：
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
