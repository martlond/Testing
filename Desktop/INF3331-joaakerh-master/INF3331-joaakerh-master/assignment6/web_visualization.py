from flask import Flask
from flask import render_template
from temperature_CO2_plotter import *

app = Flask(__name__)

@app.route("/")
def index():
    """ Displays the index page with links to temperature and CO2 plot """
    return render_template('index.html')

@app.route("/temperature")
def temperature_plot():
    """ Displays the temperature plot page """
    return render_template('temperature.html')

@app.route("/co2")
def co2_plot():
    """ Displays the CO2 plot page """
    return render_template('co2.html')

if __name__ == "__main__":
    climate = ClimateData("temperature.csv", "co2.csv")
    climate.plot_CO2(1816, 2012, None, None, False)
    climate.plot_temperature("january", 1816, 2012, None, None, False)
    app.run()
