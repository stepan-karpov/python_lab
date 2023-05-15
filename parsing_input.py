from main import Company

def ParseCompanies():
  companies = []

  input_file = open("input.in")


  for line in input_file.readlines():
    temp = line.split(" ")
    try:
      lng = float(temp[-2][:-1])
      lat = float(temp[-1])
    except:
      lng = None
      lat = None
    companies.append((lng, lat))
  
  input_file.close()
  return companies

if __name__ == "__main__":
  print(ParseCompanies()[0])
  print(ParseCompanies()[1])