import pandas as pd
diamonds = pd.read_csv("diamonds.csv")

counter = 0

for i, row in diamonds.iterrows():
  for j in range(len(row)):
    if (diamonds.iloc[i, j] == "unknown" or
        diamonds.iloc[i, j] == None):
    counter += 1

counter
