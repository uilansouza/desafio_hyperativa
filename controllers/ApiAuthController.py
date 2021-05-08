from datetime import timedelta
import jwt
import datetime
import os
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

def  process(request):

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

    user = ApiUserController().find_user(payload)
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
    return code, json_payload
    #
    #
    # check_password_hash(password, user['password'])
    #
    #
    # if  1>2:
    #     new_token = create_session_token(
    #         client_id, client['uuid'], timedelta(days=1), db)
    # else:
    #     code, json_payload = format_error_response(
    #         422,
    #         'Unprocessable Entity​​',
    #         'client_id and/or client_secret not known.'
    #     )
    #     return code, json_payload, client_id
    #
    # if not is_client_status_ok(client_id, db):
    #     code, json_payload = format_error_response(
    #         401,
    #         'Unauthorized',
    #         'Inactive client or invalid contract.'
    #     )
    #     return code, json_payload, client_id
    # expiration = 60 * 60 * 24 # one day, in seconds
    # data = {'client_id':client_id, 'session_token': new_token, 'expires_in': expiration}
    # code, json_payload = format_success_response(200, data)
    # return code, json_payload, client_id
