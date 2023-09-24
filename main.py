# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 2

# (5/5 points) Proper import of packages used.

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Dataset is downloaded from : https://www.kaggle.com/datasets/mexwell/us-school-scores

# Read the data from DataSet school_scores.csv and save it to Pandas DataFrame
schoolScores = pd.read_csv("school_scores.csv")

# Plot the Total Number of Test Takers across the United States
schoolScores.plot(x="State.Code", y="Total.Test-takers")
plotTitle = plt.title("Total Test Takers Across the United States")
plt.ylabel("Number of the Test Takers")
plt.xlabel("States")

# Saves plot
saveChart = "charts/" + plotTitle.get_text() + ".png"
plt.savefig(saveChart)

# Displays the Chart
plt.show()


# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.


# Start of the program
# It creates the chart folder
try:
    # Create the charts folder
    Path("charts").mkdir()
except FileExistsError:
    pass