from flask import Flask, render_template, jsonify, request
import requests
web_ip = "localhost:5000"
drone_id = "ABCD"
app = Flask(__name__)

def register():
    res = requests.post(web_ip + "/drone",json={"Action":"Register","ID":drone_id})
    if res.ok:
        result = res.json()
        if result["Status"] == "1" and result["DATA"]["Result"] == "1":
            return
        else:
            exit()
    else:
        exit()

def report_error():
    res = requests.post(web_ip + "/drone", json={"Action": "System_Fault", "Error_Code": 1,"GPS_Location":"22,33"})
    #TODO send stop command to drone

def get_status():
    #TODO
    return jsonify(result=1,DATA={"Result":"OK"})

def scan():
    #TODO
    return jsonify(result=1, DATA={"Result": 1})

@app.route('/request', methods=["POST"])
def scan():
    req = request.get_json()

    action = req["Action"]

    if action == 'Status':
        result = jsonify(get_status())
    elif action == "Scan":
        result = jsonify(scan())

    return result

register()
if __name__ == '__main__':
    app.run(debug=True,port=4000)
