from flask import Flask,jsonify
import requests
import datetime
import time
app = Flask(__name__)

@app.route("/get_github_repo")
def get_github_commit():
    # send a request to the github api repo
    url  = 'https://api.github.com/repos/pittcsc/Summer2024-Internships/commits'
    response  = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return jsonify({'message' : 'OOPS! Something went wrong'}), 500

    # Parse the date and time of the latest commit.
    print(datetime.datetime.strptime(data[0]['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ'))
    return jsonify({'message': 'True!!!!!'}), 200


