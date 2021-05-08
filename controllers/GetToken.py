import os
import jwt
import datetime
import logger_config

class GetToken:
    def __init__(self):
      pass;


    def get_token(self, data):
        '''
        :param data: Hash string
        :return: object
        '''
        return jwt.decode(
            data,
            os.environ.get('SECRET'),
            algorithms=["HS256"]
        )