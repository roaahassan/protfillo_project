from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "selfLearningWebsite"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import Users , Timetable
    # create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login_page"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user (id):
        return Users.query.get(int(id))

    return app


def create_db(app):
    if not path.exists('GuidedUpliftWebsit/database.db'):
        db.create_all(app = app)
        print("Create DB !")

# def create_db(app):
#     with app.app_context():
#         if not path.exists('GuidedUpliftWebsit/database.db'):
#             db.create_all()
#             print("Create DB!")
