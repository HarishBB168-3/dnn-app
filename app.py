from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

URL_NOTEPAD_ENTRY = "https://api.tatapower-ddl.com/mmg2/shownotepaddata"


def showNotepadEntry(notification):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'notification': notification
    }

    response = requests.post(URL_NOTEPAD_ENTRY, json=data, headers=headers)
    data = response.json()
    if isinstance(data, str):
        data = json.loads(response.json())
    return {
        'status_code' : response.status_code,
        'json' : data
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Thank you, {name}! We'll contact you at {email} soon."
    return render_template('contact.html')

@app.route("/notepad", methods=["GET", "POST"])
def notepad():
    if request.method == "POST":
        notification = request.form['notification']
        data = showNotepadEntry(notification)
        print(type(data['json']))
        return render_template("notepadPost.html", notification=notification, list=data['json'])
    return render_template('notepad.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
