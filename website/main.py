import sqlite3

from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from . import db, forms, json_questions, models
import secrets
import os

main = Blueprint('main', __name__)


# Creates a hex name for the picture given in the form
# Saves the new image in the profiles folder
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        main.root_path, 'static/images/profile/', 'picture_fn')
    form_picture.save(picture_path)
    return picture_fn


@main.route('/')
@main.route('/home')
def home():
    return render_template('landing.html')


@main.route('/courses')
def courses():
    return render_template('courses.html')


@main.route("/muscle")
@login_required
def muscle():
    return render_template('muscle.html')


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = forms.UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            profile_pic = save_picture(form.picture.data)
            current_user.profile_pic = profile_pic

        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email

    # profile_pic = url_for('static', filename='images/profile/' + current_user.profile_pic)
    name = current_user.name
    return render_template('profile.html', name=name, form=form)


@main.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html')


@main.route('/result')
@login_required
def end():
    return render_template('result.html')


@main.route('/questions')
@login_required
def questions():
    response = json_questions.question_bank()
    return jsonify(response)


@main.route('/score', methods=['POST'])
@login_required
def score():
    name = current_user.name
    quiz_score = request.get_json(force=True)
    if len(quiz_score) >= 1:
        score = quiz_score["score"]
        try:
            # Connecting to database
            conn = sqlite3.connect('db.sqlite3')
            # Getting cursor
            c = conn.cursor()
            # Adding data
            c.execute(
                'INSERT INTO Score (name, score) VALUES (?, ?)', [name, score])
            # Applying changes
            conn.commit()
        except:
            print("An error has occured")

        result = {"Name": name, "Score": score}
        print(f"[{result}]")
    return 'OK'


@main.route('/quiz-history', methods=['GET'])
@login_required
def marks():
    name = current_user.name
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute(
        'SELECT name AS student_name, COUNT(*) AS sumbissions, AVG(score) FROM score WHERE name = ? GROUP BY name', [name])
    marks = [dict(name=row[0], submissions=row[1], average=row[2])
             for row in c.fetchall()]
    return jsonify(marks[0])
