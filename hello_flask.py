from flask import Flask, render_template, request, redirect
from flask_analytics import Analytics

app = Flask(__name__)
Analytics(app)

app.config['GOOGLE_ANALYTICS']['ACCOUNT'] = 'UA-74115815-1'

email_addresses = []

@app.route('/emails', methods = ['GET'])
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    return redirect('/')

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
