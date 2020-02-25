import logging
from urllib.parse import urljoin

from flask import Flask, render_template
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

API_ROOT = 'https://cisco-webapp-api.herokuapp.com/api/'
app = Flask(__name__)

def api_get(endpoint):
    url = urljoin(API_ROOT, endpoint)
    logging.debug('Making API request to %s', url)
    response = requests.get(url)
    logging.debug('Response: %s', repr(response.text))
    return response.json()

@app.route('/<subreddit>')
def subreddit(subreddit):
    top_articles = api_get(f'/top/{subreddit}')['data']
    return render_template('subreddit.html', subreddit=subreddit, articles=top_articles)
