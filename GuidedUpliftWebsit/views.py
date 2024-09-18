from flask import Blueprint, render_template , request, jsonify
from flask_login import current_user , login_required
from .models import Timetable
from GuidedUpliftWebsit import db
# from flask_login import login_required
from datetime import datetime, time 

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


def convert_to_time(time_str):
   return datetime.strptime(time_str, '%H:%M').time()

@views.route("/study_timetable", methods=["GET", "POST"])
@login_required
def timetable_page():
    # all_timetables = Timetable.query.all()
    if request.method == "POST":
        data = request.get_json()
        timetable_id = data.get('id')
        day = data.get('day')
        start_time_str = data.get('stime')
        end_time_str = data.get('etime')
        std_activity = data.get('act') 
        """
        day = request.form.get('day')
        start_time_str = request.form.get('srt_tim')
        end_time_str = request.form.get('end_tim')
        std_activity = request.form.get('activity') 
        
        """
        
        start_time = convert_to_time(start_time_str)
        end_time = convert_to_time(end_time_str)

        if timetable_id:
            timetable = Timetable.query.get(timetable_id)
            if timetable:
               timetable.day = day
               timetable.start_time = start_time
               timetable.end_time = end_time
               timetable.activity = std_activity
               db.session.commit()

        else:
             timetable = Timetable(day=day,start_time=start_time,end_time=end_time,
             activity=std_activity,user_id=current_user.id)
             db.session.add(timetable)
             db.session.commit()
        return jsonify(success=True)
    # all_timetables = Timetable.query.filter_by(user=current_user.id).all()
    
    all_timetables = Timetable.query.filter_by(user_id=current_user.id).all()
    return render_template("study_timetable.html",
                           title="Study timetable",
                           custom_css="timtable",
                           user=current_user, timetables=all_timetables)
# @views.route("/add", methods=["POST"])
# def add_timetable():
#         day = request.form.get('day')
#         start_time_str = request.form.get('srt_tim')
#         end_time_str = request.form.get('end_tim')
#         std_activity = request.form.get('activity') 

#         start_time = convert_to_time(start_time_str)
#         end_time = convert_to_time(end_time_str)

#         timetable = Timetable(day=day,start_time=start_time,end_time=end_time,
#         activity=std_activity,user_id=current_user.id)
#         db.session.add(timetable)
#         db.session.commit()
        


@views.route("/edit/<int:id>", methods=["PUT"])
@login_required
def edit_timetable(id):
    data = request.get_json()
    timetable = Timetable.query.get(id)
    if timetable :
        timetable.day = data['day']
        timetable.start_time = convert_to_time(data['stime'])
        timetable.end_time = convert_to_time(data['etime'])
        timetable.activity = data['act']
        db.session.commit()
        return jsonify(success=True)
    return jsonify(error='Timetable not found'), 404

@views.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete_timetable():
    timetable = Timetable.query.get(id)
    # timetable = Timetable.query.get(timetable_id)
    if timetable:
        db.session.delete(timetable)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(error='Timetable not found'), 404

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
