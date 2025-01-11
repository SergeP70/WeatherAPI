# Building a Weather API with Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def contact(station, date):
    return {"Station: ": station,
            "Date: ": date,
            "Temperature:": 23}

if __name__ == 'main':
    app.run(debug=True)

