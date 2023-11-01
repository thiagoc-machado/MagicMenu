from rest_framework_jwt.utils import jwt_get_username_from_payload_handler
from rest_framework_jwt.authentication import jwt_decode_handler

def jwt_get_username(payload):
    return jwt_get_username_from_payload_handler(payload)

def jwt_get_payload(user):
    payload = jwt_decode_handler(user)
    payload['user_id'] = payload.get('user_id', user.pk)
    return payload