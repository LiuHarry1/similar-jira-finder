import flask
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from ui_service import *


app = Flask(__name__)
CORS(app)

app.register_blueprint(jira_searcher_pb)

@app.route('/')
def index():
    return 'welcome to my webpage!'


if __name__=="__main__":
    app.run(port=2023,host="127.0.0.1",debug=True)