import netCDF4 as nc
from os import listdir
from nameparser import parse_file

FOLDERS = (
            "GFDL-files/", 
            # "IPSL-files/",
          )

#******* Print out the first LIMIT files in each folder *************
LIMIT = 10
for folder in FOLDERS:
  path = "isimip5-files/" + folder

  for count, file in enumerate(listdir(path)):
    try:
      model, ssp, variable, start_year, end_year = parse_file(file)
    except:
      print("THIS FILE GAVE YOU A PROBLEM:", file)
      continue

    #? INSERT ANY FILERTERING HERE. 
    #? Ex: if variable == 'pr': continue (skip)

    if count == LIMIT: 
      print("==================================================")
      break
    
    #************? Do meaningful work here now for each file! **************
    try:
      print("loading: ",end="")
      print(model, ssp, variable, start_year, end_year)
      #* load in the dataset 
      ds = nc.Dataset(path + file, 'r')

      data = ds[variable+"Adjust"][0, 95:97, 217:219] 
      print(data)
    except:
      print("ERROR: skipping", path+file)

    