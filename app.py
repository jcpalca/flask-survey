from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get("/")
def survey_start():
    title = survey.title
    instructions = survey.instructions
    return render_template("survey_start.html",
                            title = title,
                            instructions = instructions)

@app.get("/questions/<int:question_id>")
def handle_questions(question_id):
    print("question_id is a ------------>>>>>>>>>>>>>>>>>>>", type(question_id))
    question = survey.questions[question_id].question
    choice = survey.questions[question_id].choices
    print("question: ------------>>>>>>>>>>>>>>>>>>>", question)
    print("choice: ------------>>>>>>>>>>>>>>>>>>>", choice)
    return render_template("question.html",
                            question = question,
                            choice = choice)
