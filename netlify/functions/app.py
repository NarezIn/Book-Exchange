from serverless_wsgi import handle_request
from app import app # the main flask file is 'app.py' and the app variable is 'app'

def handler(event, context):
    return handle_request(app, event, context)