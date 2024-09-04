from flask import Blueprint, render_template, request, redirect, url_for
# from .urls import uri_to_iri
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from GuidedUpliftWebsit import db
from sqlalchemy.exc import IntegrityError
from flask import jsonify
from flask_login import login_user, logout_user, login_required, current_user
auth = Blueprint("auth", __name__)


@auth.route('/login', methods=["GET", "POST"])
def login_page():
    """
     error = False
     if request.method == "POST":
        username = request.form.get('uname')
        password = request.form.get('upass')

        user = Users.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                 login_user(user,remember=True)
                 return redirect(url_for("views.timetable_page"))
            else: error = True
        else: error = True
    """

    return render_template("login.html",
                           title="Login Page",
                           custom_css="login_sty",
                           error=error,
                           user=current_user)


@auth.route('/create_account', methods=["GET", "POST"])
def creat_account_page():
    if request.method == "POST":
        username = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('psw')

        isNotUnique = Users.query.filter_by(username=username).first()
        if isNotUnique :
           error = True
        else:
            user = Users(username=username, email=email,
                     password=generate_password_hash(password, method="pbkdf2:sha256"))
           
            db.session.add(user)
            db.session.commit()
            
            login_user(user,remember=True)
             
        return redirect(url_for('views.home_page'))

    return render_template("create_account.html",
      custom_css="creat_acc_sty.css",
      error=error,
      user="current_user")

@auth.route("/logout")
@logout_required 
def logout():
    logout_user()
    return redirect(url_for('auth.login_page'))
