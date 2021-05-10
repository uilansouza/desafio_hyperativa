import os
import base64

from functools import wraps
from flask import request, abort
from werkzeug.exceptions import Unauthorized
from werkzeug.exceptions import Forbidden

from controllers.GetToken import GetToken

import logger_config
decode_token = GetToken()


def required_web_token_authorize(f):
    @wraps(f)
    def verify_token(*args, **kwargs):
        logger_config.get_logger()
        token = request.headers["authorization"].replace("Bearer", "").strip()
        if not token:
            raise Unauthorized()
        try:
            decode_token.get_token(token)
            return f(*args, **kwargs)
        except Exception as error:
            raise Forbidden()

    return verify_token
