# Building a Weather API with Flask
from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def contact(station, date):
    temp = 0
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["    DATE"] = pd.to_datetime(df["    DATE"])
    print(df.columns)
    print(df["    DATE"])
    temp = df.loc[df['    DATE'] == '1860-01-05 00:00:00']['   TG'].squeeze() / 10
    print(temp)


    return {"Station: ": station,
            "Date: ": date,
            "Temperature:": 23}

if __name__ == '__main__':
    app.run(debug=True)



"""
~$ python3.12 -m pip install jupyterlab
goto downloads:
Downloads$ jupyter-lab
zsh: command not found: jupyter-lab
Downloads$ python3.12 -m jupyterlab

"""