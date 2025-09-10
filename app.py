from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


# functions for analyzing as log level
@app.route("/log_level_page", methods=["POST"])
def selam():
    """
    this function renders html when clicked on
    choosing analyze style
    """
    return render_template("log_level.html")

@app.route("/analyze_as_log",methods=["POST"])
def analyze():
    """
    algorithm for analyzing at log level
    """
    return "<p> WORKIN </p>"



#functions for analyzing with date
@app.route("/date_level_page",methods=["POST"])
def analyze_date_page():
    return render_template("date_level.html")

@app.route("/analyze_as_date",methods=["POST"])
def analyze_date():
    return "<p> ANALYZING WITH DATE </p>"

if __name__ == "__main__":
    app.run(debug=True)