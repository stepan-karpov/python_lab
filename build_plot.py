from parsing_input import ParseCompanies
import matplotlib.pyplot as plt

def CreatePlot():

  for coord in ParseCompanies():
    plt.scatter(coord[0], coord[1], s=0.3)
  plt.axis([37, 38, 55.25, 56])
  plt.xlabel("Longitude")
  plt.ylabel("Latitude")
  plt.show()

def Map():
  # us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
  # us_cities = pd.read_csv()

  # print(us_cities["lat"])
  import pandas as pd
  import plotly.express as px

  us_cities = {
    "lat": [],
    "lon": []
  }

  for company in companies:
    us_cities["long"].append(company.longitude)
    us_cities["lat"].append(company.latitude)

  fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", zoom=3, height=300)
  fig.update_layout(mapbox_style="open-street-map")
  fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  fig.show()

if __name__ == "__main__":
  # CreatePlot()
  Map()