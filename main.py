# Building a Weather API with Flask
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df_stations = pd.read_csv('data/stations.txt', skiprows=17)
df_stations = df_stations[['STAID','STANAME                                 ','CN']]


@app.route("/")
def home():
    return render_template("home.html", table = df_stations.to_html(index=False))

@app.route("/api/v1/<station>/<date>")
def contact(station, date):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    response = {"Station: ": station, "Date: ": date, "Temperature:": temperature}
    return response

@app.route("/api/v1/<station>")
def station_info(station):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    response = df.to_dict(orient='records')
    return response

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)     # convert integer to string
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return result

if __name__ == '__main__':
    app.run(debug=True)



"""
~$ python3.12 -m pip install jupyterlab
goto downloads:
Downloads$ jupyter-lab
zsh: command not found: jupyter-lab
Downloads$ python3.12 -m jupyterlab

"""