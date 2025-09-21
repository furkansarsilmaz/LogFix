from flask import Flask,jsonify,request
import sqlite3

app = Flask(__name__)

@app.route("/analyze_as_log",methods=["POST"])
def log_analyze_service():
    file = request.files.get("logFile")
    if file:
        report = []
        for line in file.stream:
            decoded_line = line.decode('utf-8').lower.strip()
            if ("error" in decoded_line) :
                starter_index = decoded_line.index("error")
                report.append(decoded_line[starter_index:])
            
            elif ("warning" in decoded_line):
                starter_index = decoded_line.index("warning") 
                report.append(decoded_line[starter_index:])

        
        return jsonify({"status":"success","report":report})
    
    return jsonify({"status":"failed","message":"there is no file"})

if __name__ == "__main__" :
    app.run(port=5001)