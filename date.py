from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/analyze_as_date",methods=["POST"])
def date_analyze():
    file = request.files.get("logFile")
    if file:
        return jsonify({"status":"success","message":"service open"})
    
    
    return jsonify({"status":"failed","message":"service close"})

if __name__ == "__main__":
    app.run(port=5003)