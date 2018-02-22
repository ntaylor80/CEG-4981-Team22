from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL
from pathlib import Path
import json
import random
from Database import get_lot_info

config_name = 'config.json'

app = Flask(__name__)
Bootstrap(app)

my_file = Path(config_name)
if not my_file.is_file():
    print(config_name + " not found")
    exit()

config = json.load(open(config_name))

app.config['MYSQL_DATABASE_USER'] = config["username"]
app.config['MYSQL_DATABASE_PASSWORD'] = config["password"]
app.config['MYSQL_DATABASE_DB'] = config["database_name"]
app.config['MYSQL_DATABASE_HOST'] = config["database_ip"]

mysql = MySQL()
mysql.__init__(app)

@app.route('/')
def index():
    button_template = "<li>\n" \
                      "\t<button id=\"{}\" class=\"btn input-block-level btn-primary form-control\" type=\"button\">{}&nbsp;&nbsp;</button>\n" \
                      "</li>"

    button_block = ""
    conn = mysql.connect()
    lots = get_lot_info(conn)
    if not lots == -1:
        for lot in lots:
            button_block += button_template.format(lot[0],lot[1])
    else:
        button_block += button_template.format(1,"error")
    return render_template(('index.html'),buttons=button_block)

@app.route('/availability', methods=["POST"])
def availability():
    data = request.get_json()
    id = data["lot"]
    return jsonify(student=random.randint(0,100),faculty=random.randint(100,200),date="2018-02-20 at 17:31");


@app.route('/hello', methods=('GET', 'POST'))
def hello():
    if request.method == 'POST' or request.method == 'GET':
        data = request.get_json()

        return jsonify(('HELLO WURLD '), "test")


if __name__ == '__main__':
    app.run(debug=True)


