from urllib.parse import urljoin

from flask import Flask
import requests

API_ROOT = 'http://127.0.0.1:5000/api/'
app = Flask(__name__)

def get(endpoint):
    return requests.get(urljoin(API_ROOT, endpoint))

@app.route('/<subreddit>')
def index(subreddit):
    top_articles = get(f'/top/{subreddit}')
    return render_template('subreddit.html', subreddit=subreddit, articles=top_articles)
