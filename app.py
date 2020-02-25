import logging
from urllib.parse import urlencode, urljoin

from flask import Flask, render_template
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

API_ROOT = 'https://cisco-webapp-api.herokuapp.com/'
app = Flask(__name__)

def api_get(endpoint, **kw):
    url = urljoin(API_ROOT, endpoint)
    url += ('?' + urlencode(kw))
    logging.debug('Making API request to %s', url)
    response = requests.get(url)
    logging.debug('Response: %s', repr(response.text))
    return response.json()

@app.route('/top/<subreddit>')
def top(subreddit):
    top_articles = api_get(f'/top/{subreddit}', limit=25)['data']
    return render_template('top.html', subreddit=subreddit, articles=top_articles)
