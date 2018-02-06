from flask import Flask, render_template, request, redirect
from snowplow_tracker import Emitter, Tracker
from snowplow_tracker import SelfDescribingJson

app = Flask(__name__)

email_addresses = []
e = Emitter("localhost:8080")
t = Tracker(e, namespace="python", app_id="hello_bears")


@app.route('/emails', methods=['GET'])
def emails():
    t.track_self_describing_event(SelfDescribingJson(
        "iglu:com.hellobears/email_addresses_viewed/jsonschema/1-0-0",
        {
            "test": "stewart"
        }
    ))
    return render_template('emails.html', email_addresses=email_addresses)


@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)

    t.track_self_describing_event(SelfDescribingJson(
        "iglu:com.hellobears/email_address_submitted/jsonschema/1-0-0",
        {
            "email_address": email
        }
    ))
    return redirect('/')


@app.route('/')
def hello_world():
    t.track_page_view("www.hellobears.com", "Index")
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
