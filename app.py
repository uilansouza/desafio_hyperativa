import os
import flask
import pymongo
import datetime
import base64
import jwt

import logger_config
from decorator.token_web_authorize_jwt import required_web_token_authorize
from flask import (
    Flask,
    request,
    jsonify,
    redirect,
    url_for,
    render_template,
)
from decorator.token_web_authorize_jwt import required_web_token_authorize
from controllers import (ApiAuthController)
from controllers.ApiUserController import ApiUserController
from controllers.commons import (log_api_request,format_success_response)

MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_USER = os.getenv('MONGODB_USER')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')

app = Flask(__name__)
logger_config.configure_logger(app, __name__)
logger = logger_config.get_logger()

client = pymongo.MongoClient(os.getenv('DBAAS_MONGODB_ENDPOINT'))
db = client[MONGODB_DATABASE]
print("DB",db)


@app.route("/")
def hello():
    return jsonify({"message": "Bem vindo Desafio Hypercriativa"})


@app.route('/credicard', methods=['GET'])
@required_web_token_authorize
def autenticado():
    return jsonify({"message": "Validos"})


@app.route('/auth', methods=['POST'])
def valido():
    payload = request.get_json()
    print(payload)

    return jsonify(payload)


@app.route('/login', methods=['POST'])
def login():
    logger.info(f'login - Start endpoint login')

    http_code, json_payload = ApiAuthController.process(request)
    # log_api_request(request, http_code, client_id, db)
    logger.debug(f'AUTH - HTTP_CODE: {http_code}')
    response = app.response_class(
        response=json_payload,
        status=http_code,
        mimetype='application/json'
    )
    return response

    # payload_jwt = {
    #     "id": 1,
    #     "name": "Uilan",
    #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=180)
    # }
    #
    # token = jwt.encode(payload_jwt, os.environ.get('SECRET'), algorithm="HS256")
    #
    # return jsonify({"token": token})


@app.route('/register', methods=['POST'])
def register():

     id = ApiUserController().insert_user(request)

     return jsonify({"id":str(id)})








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, use_reloader=True)
