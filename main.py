import pandas
import plotly.figure_factory as figure_factory
import csv

df = pandas.read_csv("data.csv")
fig = figure_factory.create_distplot([df["Avg Rating"].tolist()], ["Height"], show_hist='false')
fig.show()