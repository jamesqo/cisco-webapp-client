from flask import Flask, render_template, request
import praw

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/api'
# app.config['DEBUG'] = True
# app.config['ENV'] = 'development'
reddit = praw.Reddit('webapp', config_interpolation='basic')

def pluck(obj, fields):
    return {field: getattr(obj, field) for field in fields}

def trim_submission(submission):
    result = pluck(submission, [
        'author',
        'is_self',
        'name', # TODO: What's this?
        'num_comments',
        'permalink',
        'score',
        'selftext',
        'title',
        'url'
    ])
    result['author'] = result['author'].id
    return result

@app.route('/top/<subreddit>')
def top(subreddit):
    limit = request.args.get('limit', 10)
    if subreddit is None:
        return {'error': 'Please specify a subreddit.'}, 400

    submissions = reddit.subreddit(subreddit).top(limit=limit) # TODO: Get all of them (lazily load)
    submissions = list(map(trim_submission, submissions))
    return {
        'data': submissions
    }
