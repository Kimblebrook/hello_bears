from flask import Flask, render_template, request, redirect
from snowplow_tracker import Subject, Emitter, Tracker

app = Flask(__name__)

email_addresses = []
e = Emitter("localhost:8080", namespace="python", app_id="hello_bears")
t = Tracker(e)


@app.route('/emails', methods=['GET'])
def emails():
    return render_template('emails.html', email_addresses=email_addresses)


@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    return redirect('/')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
