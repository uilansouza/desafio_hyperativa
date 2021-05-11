import os
import logger_config
from flask import (
    Flask,
    request,
    jsonify,

)
from decorator.token_web_authorize_jwt import required_web_token_authorize
from controllers import (ApiAuthController, ApiCardController)
from controllers.ApiUserController import ApiUserController

app = Flask(__name__)
logger_config.configure_logger(app, __name__)
logger = logger_config.get_logger()


@app.route("/")
def hello():
    return jsonify({"message": "Bem vindo Desafio Hypercriativa"})


@app.route('/card', methods=['POST'])
@required_web_token_authorize
def card():
        http_code, json_payload = ApiCardController.post_card(request)
        logger.debug(f'AUTH - HTTP_CODE: {http_code}')
        response = app.response_class(
            response=json_payload,
            status=http_code,
            mimetype='application/json'
        )
        return response

@app.route("/card/<id>", methods=['GET'])
@required_web_token_authorize
def get_one_card(id):
    http_code, json_payload = ApiCardController.get_card(id)
    logger.debug(f'AUTH - HTTP_CODE: {http_code}')
    response = app.response_class(
        response=json_payload,
        status=http_code,
        mimetype='application/json'
    )
    return response

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
