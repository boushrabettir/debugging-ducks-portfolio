import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from app.utils import User
from app.map import MAP_HTML
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict


load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING")=="true":
    mydb=SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:   
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

print(mydb)

class TimelinePost(Model):
    name=CharField()
    email=CharField()
    content=CharField()
    created_at=DateTimeField(default=datetime.datetime.now)

    class Meta:
        database=mydb

mydb.connect()
mydb.create_tables([TimelinePost])



@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    data=request.get_json()
    if not data:
        return jsonify({"error": "Invalid"}), 400
    print(data)
    name=data.get('name')
    email=data.get('email')
    content=data.get('content')

    if not name:
        return jsonify(error="Invalid name"), 400
    if not content:
        return jsonify(error="Invalid content"), 400
    if '@' not in email:
        return jsonify(error="Invalid email"), 400

    timeline_post=TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
    
user = User()

URL = "http://127.0.0.1:5000"
PAGES = [
    {"name": "Education", "href": f"{URL}/education"},
    {"name": "Work Experience", "href": f"{URL}/work_experience"},
    {"name": "Hobbies", "href": f"{URL}/hobbies"},
    {"name": "Projects", "href": f"{URL}/projects"},
    ]
    
@app.route('/', endpoint='index')
def index():
    return render_template('index.html',
                           education=user.education,
                           work_experience=user.work_experience,
                           hobbies=user.hobbies,
                           title="MLH Fellow",
                           MAP_HTML=MAP_HTML,
                           url=os.getenv("URL"),
                           pages=PAGES)

@app.route('/projects')
def projects():
    return render_template('projects.html',
                           projects=user.projects)

@app.route('/education')
def education():
    return render_template('education.html',
                           education=user.education
                           )

@app.route('/work_experience')
def work_experience():
    return render_template('work_exp.html',
                           work_experience=user.work_experience)

@app.route('/hobbies', endpoint='hobbies')
def hobbies():
    return render_template('hobbies.html',
                           hobbies=user.hobbies,
                           url=os.getenv("URL"))

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")