import os
from app import logger_config

from ..controllers.commons import(
    generate_password_hash,
    verify_password,
    format_error_response,
    format_success_response
)
from ..model.Card import Card

def post_card(request):
    logger = logger_config.get_logger()
    payload = request.get_json()
    if not payload:
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'No payload.'
        )
        return code, json_payload
    fields_required = ["card"]

    for fields in fields_required:
        if not payload.get(fields):
            code, json_payload = format_error_response(
                400,
                'Bad Request​',
                f'field {fields} is required'
            )
            return code, json_payload

    if len(payload['card']) <= int(os.getenv('DIGITS')):
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            f'nnumber must be greater than {os.getenv("DIGITS")} characters'
        )
        return code, json_payload
    if not payload['card'].isdigit():
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'Only caracter number'
        )
        return code, json_payload

    payload['hash_card'] = generate_password_hash(payload['card'])
    numbers_card = payload['card']
    payload['card'] = f'{numbers_card[:4]}*****{numbers_card[-4:]}'
    try:
        logger.info('Card - card successfully registered ')
        id = Card().insert_card(payload)
        data = {"id": str(id)}
        code, json_payload = format_success_response(201, data)

        return code, json_payload
    except Exception as error:
        logger.error('Card - Error register card ')
        return 500, error

def get_card(number_card):
    logger = logger_config.get_logger()
    user_card = f'{number_card[:4]}*****{number_card[-4:]}'
    base_card = Card().find_card({"card": user_card})

    if not base_card:
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            f'Card Not Found'
        )
        return code, json_payload

    if not verify_password(base_card['hash_card'], number_card):
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            'number card invalid'
        )
        return code, json_payload
    if not base_card:
        code, json_payload = format_error_response(
            400,
            'Bad Request​',
            f'Card Not Found'
        )
        return code, json_payload
    data = {"id": str(base_card['_id']), "card": user_card}
    code, json_payload = format_success_response(200, data)
    logger.info('Card - Get card successfully')
    return code, json_payload