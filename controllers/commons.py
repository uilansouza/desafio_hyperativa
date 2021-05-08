import datetime
import json
from werkzeug.security import check_password_hash, generate_password_hash

def log_api_request(request, http_code, client_id, db):
    db['logs'].insert_one({
        'timestamp': datetime.now(),
        'service': 'API',
        'category': 'INFO',
        'request': '{} {}'.format(request.method, request.full_path),
        'http_code': http_code,
        'client_id': client_id if client_id else ''
    })

def format_error_response(code, title, description):
    contents = {'title': title, 'description': description}
    json_payload = json.dumps(contents, ensure_ascii=False).encode('utf8')
    return code, json_payload

def format_success_response(code, payload=None):
    json_payload = json.dumps(payload),
    return code, json_payload

def generate_hash_password(password):
    return generate_password_hash(password)

def verify_password(hash_password,password):
    print("hash:  ", hash_password)
    print("password:  ", password)
    return check_password_hash(hash_password, password)

