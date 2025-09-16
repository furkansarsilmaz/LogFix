from flask import Flask,jsonify,request
import requests

app = Flask(__name__)

@app.route("/saved",methods=["POST"])
def saved():
    data = request.get_json()
    report = data.get("report",[])
    with open ("reports.txt","w") as file:
        for line in report:
            file.write(line + "\n")



if __name__ == "__main__" :
    app.run(port=5002)