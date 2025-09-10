from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/log_level_page", methods=["POST"])
def selam():
    return render_template("log_level.html")

@app.route("/analyze_as_log",methods=["POST"])
def analyze():
    return "<p> WORKIN </p>"

@app.route("/analyze",methods=["POST"])
def analyze_2():
    return "<p> ITS GONNA LOOK FOR DATES ON ANALYZE </p>"

if __name__ == "__main__":
    app.run(debug=True)