from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/analyze_as_date",methods=["POST"])
def date_analyze():
    file = request.files.get("logFile")
    index_of_user = request.form.get("User_Input")
    if file and index_of_user :
        report = []
        for line in file.stream:
            decoded_line = line.decode('utf-8')
            if index_of_user in decoded_line:
                starter_index = decoded_line.index(index_of_user)
                report.append(decoded_line[starter_index:])

        return jsonify({"status":"success","message":report})
    

    return jsonify({"status":"failed","message":"service close"})

if __name__ == "__main__":
    app.run(port=5003)