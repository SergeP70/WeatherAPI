# Building a Weather API with Flask
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df_stations = pd.read_csv('data/stations.txt', skiprows=17)
df_stations = df_stations[['STAID','STANAME                                 ','CN']]

print(df_stations)



@app.route("/")
def home():
    return render_template("home.html", table = df_stations.to_html())

@app.route("/api/v1/<station>/<date>")
def contact(station, date):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == "1860-01-05"]['   TG'].squeeze()/10
    print(temperature)
    print(type(temperature))

    return {"Station: ": station,
            "Date: ": date,
            "Temperature:": temperature}

if __name__ == '__main__':
    app.run(debug=True)



"""
~$ python3.12 -m pip install jupyterlab
goto downloads:
Downloads$ jupyter-lab
zsh: command not found: jupyter-lab
Downloads$ python3.12 -m jupyterlab

"""