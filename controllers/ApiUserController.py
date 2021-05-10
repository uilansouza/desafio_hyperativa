
import requests
import json
from model.Usuario import User
from controllers.commons import check_password_hash,generate_password_hash

class ApiUserController:
    def __init__(self):
        self.user = User()

    def post_user(self, request):

        payload = request.get_json()
        if not payload:
            return {"message": " payload is required"}, 404
        fields_required = ["username", "password"]
        for fields in fields_required:
            if not payload.get(fields):
                return {"message": f"field {fields} is required"}
        payload['password'] = generate_password_hash(payload['password'])
        return self.user.insert_user(payload)

    def get_user(self, data):
       return self.user.find_user({"username": data['username']})

