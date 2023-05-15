import requests
from time import sleep

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Company:
  name = "default name"
  longitude = None
  latitude = None
  def __init__(self, name: str, longitude: float, latitude: float) -> None:
    self.name = name
    self.longitude = longitude
    self.latitude = latitude

if __name__ == "__main__":
    URL = 'https://api.hh.ru/vacancies'

    params = {
      'text': "2286969",
      'area': 1,
      'page': 0,
      'per_page': 20
    }

    # interesting_jobs = ["Уборщик", "Водитель мусоровоза", "Продавец",
    #                     "Курьер", "Web-дизайнер"]
    interesting_jobs = ["Уборщик"]

    companies = []

    for job in interesting_jobs:
      params["text"] = job
      params["page"] = 0
      params["per_page"] = 10
      data = requests.get(URL, params).json()
      print("---->" + job + ": " + str(data["pages"]) + " pages\n\n")
      for page in range(0, data["pages"]):
        params["page"] = page
        data = requests.get(URL, params).json()
        sleep(0.1)
        for item in data["items"]:
          name = item["employer"]["name"]
          try:
            longitude = item["address"]["lng"]
            latitude = item["address"]["lat"]
          except:
            longitude = None
            latitude = None
            
          company_to_add = Company(name, None, None)
          companies.append(company_to_add)
          print(company_to_add.name + " " + company_to_add.longitude + ", " + company_to_add.latitude)
      print("----->   done with this job !!!")