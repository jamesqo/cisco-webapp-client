from urllib.parse import urljoin

from flask import Flask
import requests

API_ROOT = 'https://cisco-webapp-api.herokuapp.com/api/'
app = Flask(__name__)

def api_get(endpoint):
    return requests.get(urljoin(API_ROOT, endpoint))

@app.route('/<subreddit>')
def subreddit(subreddit):
    top_articles = get(f'/top/{subreddit}')
    return render_template('subreddit.html', subreddit=subreddit, articles=top_articles)
