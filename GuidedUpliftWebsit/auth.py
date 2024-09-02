from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from GuidedUpliftWebsit import db
from sqlalchemy.exc import IntegrityError
from flask import jsonify
auth = Blueprint("auth", __name__)


@auth.route('/login', methods=["GET", "POST"])
def login_page():
    # if request.method == "POST":
    #     username = request.form.get('uname')
    #     password = request.form.get('upass')

    #     user = Users.query.filter_by(username=username).first()
    #     if user:
    #         if check_password_hash(user.password, password):
    #             return redirect(url_for("views.timetable_page"))

    return render_template("login.html",
                           title="Login Page",
                           custom_css="login_sty")


@auth.route('/create_account', methods=["GET", "POST"])
def creat_account_page():
    if request.method == "POST":
        username = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('psw')

        if Users.query.filter_by(username=username).first():
            return jsonify({'success': False, 'message': 'Username already taken'}), 400

        user = Users(username=username, email=email,
                     password=generate_password_hash(password, method="pbkdf2:sha256"))
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Account created'})
        except IntegrityError:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error creating account'}), 500

        #  return redirect(url_for('login_page'))

    return render_template("create_account.html", custom_css="creat_acc_sty.css")
