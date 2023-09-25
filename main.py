# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def readDataSet():
    # Dataset is downloaded from : https://www.kaggle.com/datasets/mexwell/us-school-scores
    # Read the data from DataSet school_scores.csv and save it to Pandas DataFrame
    schoolScores = pd.read_csv("school_scores.csv",index_col="Year")


    # It shows a quick statistic summary of the dataset.
    stats = schoolScores.describe()
    print(stats)
    return schoolScores

def generateChart():
    grouped = pd.DataFrame(readDataSet()).groupby("State.Code")["Total.Test-takers"].sum()

    # Generate a bar chart
    # Sets the size of the figure.
    plt.figure(figsize=(10, 5))
    # Type of the figure is set to Bar.
    plt.bar(grouped.index, grouped.values)
    chartTitle = plt.title("Total Number of Test Takers by State")
    plt.xlabel("States")
    plt.ylabel("Total Test Takers")
    # Turns the States Codes 90 degree upwards.
    plt.xticks(rotation=90)
    # Axes on the figure adjusted to avoid the overlaying content.
    plt.tight_layout()

    # Saves plot
    saveChart = "charts/" + chartTitle.get_text() + ".png"
    plt.savefig(saveChart)

    # Displays the Chart
    plt.show()



# It creates the chart folder
try:
    # Create the charts folder
    Path("charts").mkdir()
except FileExistsError:
    pass

# Start of the program
readDataSet()
generateChart()