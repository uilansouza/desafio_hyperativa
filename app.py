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
from controllers import (ApiAuthController, ApiCardController)
from controllers.ApiUserController import ApiUserController
from controllers.commons import (log_api_request,format_success_response)

app = Flask(__name__)
logger_config.configure_logger(app, __name__)
logger = logger_config.get_logger()


@app.route("/")
def hello():
    return jsonify({"message": "Bem vindo Desafio Hypercriativa"})


@app.route('/card', methods=['GET','POST'])
@required_web_token_authorize
def card():

    # logger.debug(f'AUTH - HTTP_CODE: {http_code}')
    # response = app.response_class(
    #     response=json_payload,
    #     status=http_code,
    #     mimetype='application/json'
    # )
    # return response
    return jsonify({"message": "Validos"})




@app.route('/login', methods=['POST'])
def login():
    logger.info(f'login - Start endpoint login')

    http_code, json_payload = ApiAuthController.process_login(request)
    logger.debug(f'AUTH - HTTP_CODE: {http_code}')
    response = app.response_class(
        response=json_payload,
        status=http_code,
        mimetype='application/json'
    )
    return response


@app.route('/register', methods=['POST'])
def register():

     id = ApiUserController().post_user(request)

     return jsonify({"message": str(id)})








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True, use_reloader=True)
