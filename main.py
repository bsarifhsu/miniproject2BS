# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Dataset is downloaded from : https://www.kaggle.com/datasets/mexwell/us-school-scores
# Read the data from DataSet school_scores.csv and save it to Pandas DataFrame
schoolScores = pd.read_csv("school_scores.csv")


# Plot the Total Number of Test Takers across the United States
schoolScores.plot(x="State.Code", y="Total.Test-takers")
chartTitle = plt.title("Total Test Takers Across the United States")
plt.ylabel("Test Takers")
plt.xlabel("States")


# Saves plot
saveChart = "charts/" + chartTitle.get_text() + ".png"
plt.savefig(saveChart)

# Displays the Chart
plt.show()


# Start of the program

# It creates the chart folder
try:
    # Create the charts folder
    Path("charts").mkdir()
except FileExistsError:
    pass