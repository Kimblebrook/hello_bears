from flask import Flask, render_template, request, redirect

app = Flask(__name__)

email_addresses = []


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
