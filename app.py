from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

SESSION_KEY = "responses"

@app.get("/")
def survey_start():
    """
    displays home page of starting survey for user
    """

    session[SESSION_KEY] = []

    title = survey.title
    instructions = survey.instructions
    return render_template(
        "survey_start.html",
        title = title,
        instructions = instructions
        )

@app.post("/begin")
def redirect_questions():
    """
    redirects to first question
    """

    return redirect('/questions/0')


@app.get('/questions/<int:question_id>')
def handle_questions(question_id):
    """
    displays question, choice buttons, and Continue button
    """

    print("question_id is a ------------>>>>>>>>>>>>>>>>>>>", type(question_id))
    question = survey.questions[question_id]
    print("question: ------------>>>>>>>>>>>>>>>>>>>", question)
    return render_template("question.html",
                            question = question)

@app.post('/answer')
def redirect_answers():
    """
    redirect to next question until last question and then moves to complete pg.
    """

    answer = request.form['answer']
    responses = session[SESSION_KEY]
    responses.append(answer)
    session[SESSION_KEY] = responses

    if len(responses) < len(survey.questions):
        return redirect(f'/questions/{len(responses)}')
    else:
        return redirect('/complete')


@app.get('/complete')
def complete():
    """
    displays completion page
    """

    questions = survey.questions
    len_questions = len(questions)
    responses = session[SESSION_KEY]

    return render_template('completion.html',
                            responses = responses,
                            questions = questions,
                            len_questions = len_questions)
