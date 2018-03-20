from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL
from pathlib import Path
import json
import Database as db
from image import analyze_image

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

drones = {}

@app.route('/drone',methods=["POST"])
def drone():
    data = request.get_json()
    action = data["Action"]

    if action == "Register":
        id = data["ID"]
        drones[id] = Drone(id)
        result = jsonify(Result=1)
    elif action == "Update":
        id = data["ID"]
        status = data["Status"]
        drones[id].status = status_values[status]
        result = jsonify(Result=1)
    elif action == "Analyze":
        lot = data["Lot"]
        image = data["Image"]
        #TODO process image
        result = jsonify(Result=1)
    elif action == "System_Fault":
        #TODO process error
        result = jsonify(Result=1)
    else:
        return jsonify(Status=0)

    return jsonify(Status = 1,DATA=result)

@app.route('/')
def index():
    button_template = "<li>\n" \
                      "\t<button id=\"{}\" class=\"btn input-block-level btn-primary form-control\" type=\"button\">{}&nbsp;&nbsp;</button>\n" \
                      "</li>"

    button_block = ""
    conn = mysql.connect()
    lots = db.get_lot_info(conn)

    if not lots == -1:
        for lot in lots:
            button_block += button_template.format(lot[0],lot[1])
    else:
        button_block += button_template.format(1,"error")
    conn.close()
    return render_template(('index.html'),buttons=button_block)

@app.route('/availability', methods=["POST"])
def availability():
    data = request.get_json()
    id = data["lot"]
    conn = mysql.connect()
    data = db.get_lot_status(conn, id)
    conn.close()
    if data:
        result =jsonify(success=1,student=data["student"],faculty=data["faculty"],date=data["date"])
    else:
        result = jsonify(success=0)
    return result

@app.route('/update',methods=['POST'])
def update():
    data = request.get_json()

    if 'image' in data and 'lot' in data:
        conn = mysql.connect()
        lots = analyze_image(data['image'])
        db.update_lot(conn,lots[0],lots[1],data['lot'])
        conn.close()
        return jsonify(result="1")

@app.route('/hello', methods=('GET', 'POST'))
def hello():
    if request.method == 'POST' or request.method == 'GET':
        data = request.get_json()

        return jsonify(('HELLO WURLD '), "test")


if __name__ == '__main__':
    app.run(debug=True)


