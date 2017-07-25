from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello from uwsgi'

