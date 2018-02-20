from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template(('index.html'))

@app.route('/availability', methods=["POST"])
def availability():
    data = request.get_json()
    id = data["lot"]
    return jsonify(test=id)


@app.route('/hello', methods=('GET', 'POST'))
def hello():
    if request.method == 'POST' or request.method == 'GET':
        data = request.get_json()

        return jsonify(('HELLO WURLD '), "test")


if __name__ == '__main__':
    app.run(debug=True)


