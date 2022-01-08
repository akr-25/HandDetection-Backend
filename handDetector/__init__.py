from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from handDetector.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = PyMongo(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from handDetector.auth.routes import auth
from handDetector.user.routes import user


app.register_blueprint(auth)
app.register_blueprint(user)




# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager = LoginManager()


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)

#     from handDetector.auth.routes import auth
#     from handDetector.user.routes import user


#     app.register_blueprint(auth)
#     app.register_blueprint(user)

#     return app
