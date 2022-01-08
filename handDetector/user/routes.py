from flask import request, Blueprint

user = Blueprint('user', __name__)

@user.route('/us', methods=['GET'])
def test():
    print(request.json)
    return "Hello User"