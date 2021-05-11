import logging
from datetime import timedelta
import jwt
import datetime
import os
import logger_config
from controllers.ApiUserController import ApiUserController
from controllers.commons import(
    generate_hash_password,
    verify_password,
    check_password_hash,
    # is_client_status_ok,
    format_error_response,
    format_success_response
)

# --------------------

def  process_login(request):
    logger = logger_config.get_logger()
    payload = request.get_json()
    if not payload:
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'No payload.'
        )
        return code, json_payload
    if not payload.get('username') or not payload.get("password"):
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'Missing members: username and/or password.'
        )
        return code, json_payload

    if not ApiUserController().get_user(payload):
        code, json_payload = format_error_response(
            404,
            'Bad Request​',
            'username not found',
        )
        return code, json_payload

    user = ApiUserController().get_user(payload)
    username = payload['username']
    password = payload['password']

    if not verify_password(user['password'], password):
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'username and/or password is Invalid'
        )
        return code, json_payload

    payload_jwt = {
        "id": 1,
        "username": username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=180)
    }

    token = jwt.encode(payload_jwt, os.environ.get('SECRET'), algorithm="HS256")
    data = {"id": user['username'], "token":token}
    code, json_payload = format_success_response(200, data)
    logger.info(f" Login - User authentication success")
    return code, json_payload

