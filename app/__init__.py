import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

from jinja2 import Environment, FileSystemLoader

load_dotenv()
app = Flask(__name__)

hobbies = ["Football", "Video Games", "Watching Aurora"]
work_experience = ["SWE @ Incorta     2021-2024", "SWE Intern @ M3ntorship      01/2021-04/2021"]
education = ["M.Sc. @ TTU     2024-2026", "B.Sc. @ Alexandria University    2026-2021"]

@app.route('/')
def index():
    return render_template('index.html', education=education, work_experience=work_experience, hobbies=hobbies, title="MLH Fellow", url=os.getenv("URL"))
