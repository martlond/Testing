import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ClimateData:
    """ Class for reading climate data from CSV files and generating plots. """
    def __init__(self, temperature_file, co2_file):
        """ Reads from files and initializes the Pandas data structures.
        Inputs:
            temperature_file (str)    - path to .csv file containing
                                        temperature data
            co2_file (str)            - path to .csv file containing co2 data
        """

        self.temperature_data = pd.read_csv(temperature_file,
                                            sep = ",").set_index("Year")
        self.co2_data = pd.read_csv(co2_file, sep = ",").set_index("Year")

    def plot_CO2(self, t_start, t_end, y_min = None,
                 y_max = None, show = True):
        """ Method for plotting CO2 data per year.
        Inputs:
            t_start (int) - Year to start plotting from
            t_end (int)   - Year to plot until
        Optional inputs:
            y_min (int)   - y_axis minimum value for the plot
                            Default: minimum CO2 value in the range divided
                                     by 1.3
            y_max (int)   - y_axis maximum value for the plot
                            Default: maximum CO2 value in the range multiplied
                                     by 1.15
            show (bool)   - Whether or not to display the plot. Default: True
        """
        if t_end <= t_start:
            print("End time can't be smaller than or equal to start time")
            return

        co2_data = self.co2_data
        min_year = co2_data.index.min()
        max_year = co2_data.index.max()

        if t_start < min_year or t_end > max_year:
            print("Year input out of bounds, earliest year is:", min_year)
            print("Latest year is:", max_year)
            return

        co2_data = co2_data.loc[t_start:t_end]

        if not y_min:
            y_min = co2_data["Carbon"].min() / 1.3
        if not y_max:
            y_max = co2_data["Carbon"].max() * 1.15

        co2_data.plot(y = "Carbon")
        plt.ylim(y_min, y_max)
        plt.title("Atmospheric CO2 per year")
        plt.ylabel("CO2")
        plt.savefig("static/co2.png")
        if show:
            plt.show()
        else:
            plt.close()

    def plot_temperature(self, month, t_start, t_end, y_min = None,
                         y_max = None, show = True):
        """ Method for plotting temperature data per year.
        Inputs:
            month (str)   - Which month to plot temperature data for
            t_start (int) - Year to start plotting from
            t_end (int)   - Year to plot until
        Optional inputs:
            y_min (int)   - y_axis minimum value for the plot
                            Default: minimum temp value in the range multiplied
                                     by 1.2 (divided by 1.2 if > 0)
            y_max (int)   - y_axis maximum value for the plot
                            Default: maximum temp value in the range multiplied
                                     by 1.2
            show (bool)   - Whether or not to display the plot. Default: True
        """
        if t_end <= t_start:
            print("End time can't be smaller than or equal to start time")
            return

        temperature_data = self.temperature_data
        min_year = temperature_data.index.min()
        max_year = temperature_data.index.max()

        if t_start < min_year or t_end > max_year:
            print("Year input out of bounds, earliest year is:", min_year)
            print("Latest year is:", max_year)
            return

        # Make month input proper case, i.e. capital first letter and the rest
        # lower case, to match column titles in the data file
        month = month.title()

        try:
            temperature_data = temperature_data[month].loc[t_start:t_end]
        except Exception as e:
            print("Couldn't parse month and time input.")
            print("Make sure month input is correct:", e)
            return

        if not y_min:
            y_min = temperature_data.min()
            if y_min > 0:
                y_min /= 1.2
            else:
                y_min *= 1.2
        if not y_max:
            y_max = temperature_data.max() * 1.2

        temperature_data.plot()
        plt.ylim(y_min, y_max)
        plt.legend(["Temperature"])
        plt.title("Temperature per year for " + month)
        plt.ylabel("Temperature [C]")
        plt.savefig("static/temp.png")
        if show:
            plt.show()
        else:
            plt.close()


if __name__ == "__main__":
    """ Main block of program """
    climate = ClimateData("temperature.csv", "co2.csv")
    climate.plot_CO2(1816, 2012)
    climate.plot_temperature("february", 1816, 2012)
