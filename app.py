from urllib.parse import urljoin

from flask import Flask, render_template
import requests

API_ROOT = 'https://cisco-webapp-api.herokuapp.com/api/'
app = Flask(__name__)

def api_get(endpoint):
    response = requests.get(urljoin(API_ROOT, endpoint))
    return response.json()

@app.route('/<subreddit>')
def subreddit(subreddit):
    top_articles = api_get(f'/top/{subreddit}')['data']
    return render_template('subreddit.html', subreddit=subreddit, articles=top_articles)
