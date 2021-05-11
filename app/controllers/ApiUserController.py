
from ..model.Usuario import User
from ..controllers.commons import check_password_hash,generate_password_hash
from app import logger_config
class ApiUserController:
    def __init__(self):
        self.user = User()

    def post_user(self, request):
        logger = logger_config.get_logger()
        payload = request.get_json()
        if not payload:
            return {"message": " payload is required"}, 404
        fields_required = ["username", "password"]
        for fields in fields_required:
            if not payload.get(fields):
                return {"message": f"field {fields} is required"}
        payload['password'] = generate_password_hash(payload['password'])
        logger.info(f" User - User created success")
        return self.user.insert_user(payload)

    def get_user(self, data):
       logger = logger_config.get_logger()
       logger.info(f" User - Get - User  success")
       return self.user.find_user({"username": data['username']})
