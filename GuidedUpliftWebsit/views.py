from flask import Blueprint, render_template , request
from flask_login import current_user
from .models import Timetable
from GuidedUpliftWebsit import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home_page():
    return render_template("home.html",
                           title="Home Page",
                           navbar=True,
                           custom_css="home_sty")


@views.route("/std_org")
def study_org():
    return render_template("std_org.html",
                           title="Study Organization Page",
                           navbar=True,
                           custom_css="std_org_sty")


@views.route("/study_timetable", methods=["GET", "POST"])
@login_required
def timetable_page():
    all_posts = Post.query.all()
    if request.method == "POST":
        day = request.form.get('day')
        time = request.form.get('time')
        subject = request.form.get('subject')

        timetable = Timetable(day=day,time=time,subject=subject,
        user_id=current_user.id, posts=all_posts)

        db.session.add(timetable)
        db.session.commit()

    return render_template("study_timetable.html",
                           title="Study timetable",
                           custom_css="timtable",
                           user=current_user)


@views.route("/learn_tech_mem")
def learn_tech_mem_page():
    return render_template("learn_tech_mem.html",
                           title="Learning Techniuqes/Memory",
                           navbar=True,
                           custom_css="learn_tech_mem_sty")


@views.route("/books")
def books_page():
    return render_template("books.html",
                           title="Books Page",
                           navbar=True,
                           custom_css="books_sty",)


# from flask import Flask, render_template


# guidedUplift_app = Flask(__name__)


# @guidedUplift_app.route("/")
# def loginpage():
#     return render_template("login.html")


# @guidedUplift_app.route("/create_account")
# def create_acount_page():
#     return render_template("create_account.html")


# # @guidedUplift_app.route("/create_account/login")
# # def load_login_page():
# #     return render_template("login.html")


# @guidedUplift_app.route("/home")
# def homepage():
#     return render_template("home.html", custom_css="home_sty")


# @guidedUplift_app.route("/home/std_org")
# def studypage():
#     return render_template("std_org.html", custom_css="std_org_sty")


# @guidedUplift_app.route("/home/study_timetable")
# def timetablepage():
#     return render_template("study_timetable.html",
#                            title="Study timetable",
#                            custom_css="timtable")


# @guidedUplift_app.route("/home/learn_tech_mem")
# def learn_techniquespage():
#     return render_template("learn_tech_mem.html",
#                            title="Learning Tech & memory",
#                            custom_css="learn_tech_mem_sty")


# @guidedUplift_app.route("/home/books")
# def bookspage():
#     return render_template("books.html", title="books",  custom_css="books_sty")


# if __name__ == "__main__":
#     guidedUplift_app.run(debug=True)
