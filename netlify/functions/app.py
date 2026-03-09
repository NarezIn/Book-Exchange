import sys
import os
from serverless_wsgi import handle_request

# Add the project root to the python path so we can import app and database
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app # the main flask file is 'app.py' and the app variable is 'app'

def handler(event, context):
    return handle_request(app, event, context)
