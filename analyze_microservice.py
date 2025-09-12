from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/analyze_as_log",methods=["POST"])
def log_analyze_service():
    file = request.file.get("logFile")
    if file:
        return jsonify({"status":"success","message":"working"})
    return jsonify({"status":"failed","message":"there is no file"})

if "__name__" == "__main__" :
    app.run()