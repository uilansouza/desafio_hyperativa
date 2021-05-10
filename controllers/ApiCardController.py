
from controllers.commons import(
    generate_password_hash,
    verify_password,

    format_error_response,
    format_success_response
)

def post_card(request):
    payload = request.get_json()
    if not payload:
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'No payload.'
        )
        return code, json_payload
    fields_required = ["username", "password"]
    for fields in fields_required:
        if not payload.get(fields):
            return {"message": f"field {fields} is required"}

    if not int(payload['card']):
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'Only caracter number'
        )
        return code, json_payload

    payload['card'] = generate_password_hash(payload['card'])



