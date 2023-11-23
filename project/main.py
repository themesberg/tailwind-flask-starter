# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('staticPages/index.html',var1='toto')

@main.route("/about")
def about():
	return render_template("staticPages/about.html")

@main.route('/tourdecontrol')
@login_required
def tourdecontrol():
    user_id = current_user.get_id()
    username = current_user.name
    timelines = [user_id,
                username,
                'This is the third event.'
                ]
    return render_template("boardPages/tourdecontrol.html",timelines=timelines, user=current_user)
