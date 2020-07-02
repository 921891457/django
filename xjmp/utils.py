from rest_framework.response import Response

def reformat_resp(code, body, message=''):
    data = {
        'code': code,
        'body': body,
        'message': message
    }
    resp = Response(data)
    return resp
