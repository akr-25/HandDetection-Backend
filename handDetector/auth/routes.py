from flask import request, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/au', methods=['GET'])
def test():
    print(request.json)
    return "Hello"