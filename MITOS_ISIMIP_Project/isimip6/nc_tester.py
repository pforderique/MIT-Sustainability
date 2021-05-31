import netCDF4 as nc
from os import listdir
from math import ceil, floor
from nameparser import parse_file
from mapper import coor_to_grid

#* MIT Coordinates and resulting 2x2 grid bounds surrounding campus
MIT_COOR  = (42.3588, -71.0934)
GRID_COOR = coor_to_grid(*MIT_COOR)

UPPER_GRID_LAT = ceil(GRID_COOR[0])
LOWER_GRID_LAT =  floor(GRID_COOR[0])
UPPER_GRID_LON = ceil(GRID_COOR[1])
LOWER_GRID_LON =  floor(GRID_COOR[1])

FOLDERS = (
            "GFDL-files/", 
            "MPI-files/",
            "UKESM-files/",
            "IPSL-files/",
            "MRI-files/",
            "wget-mitos/",
          )

#******* Print out the first LIMIT files in each folder *************
LIMIT = 10
for folder in FOLDERS:
  path = "isimip-files/" + folder

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
      print(model, ssp, variable, start_year, end_year)
    except:
      print("ERROR: skipping", path+file)

    # #* load in the dataset 
    ds = nc.Dataset(path + file, 'r')

    #* this is precips = ds['pr'][0, 95:97, 217:219] 
    precips = ds[variable][1, LOWER_GRID_LAT:UPPER_GRID_LAT+1, LOWER_GRID_LON:UPPER_GRID_LON+1] 
    print(precips)