# Building a Weather API with Flask
from flask import Flask, render_template

app = Flask("WeatherAPI")

@app.route("/home")
def home():
    return render_template("tutorial.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)

