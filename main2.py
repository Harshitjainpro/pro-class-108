import csv
import pandas as p
import plotly.figure_factory as pff

df = p.read_csv("data.csv")
fig = pff.create_distplot([df["Avg Rating"].tolist()],["AVG RATING"],show_hist=False)
fig.show()