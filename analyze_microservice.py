from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/analyze_as_log",methods=["POST"])
def log_analyze_service():
    file = request.files.get("logFile")
    if file:
        report = []
        for line in file.stream:
            decoded_line = line.decode('utf-8').strip()
            report.append(decoded_line)

        return jsonify({"status":"success","report":report})
    return jsonify({"status":"failed","message":"there is no file"})

if __name__ == "__main__" :
    app.run(port=5001)