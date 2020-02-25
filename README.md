# cisco-webapp-client

This repo contains the client-side code for the web app. It calls into the Heroku API endpoint defined by the other repo, fetches and deserializes the results, then uses them to render an HTML response. I used https://www.gradient-animator.com/ to help me generate the background effect.

## Frameworks Used

- Flask
- Requests

## Instructions

```
export FLASK_APP=app.py

pip install -r requirements.txt
flask run
```

Python 3.6+ is required.

## Demonstration

http://cisco-webapp-client.herokuapp.com/top/askreddit
