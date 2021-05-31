import netCDF4 as nc
import numpy as np
from os import listdir

print("++++++++\nTRANSFER STARTED\n++++++++\n")

FOLDERS = (
            "GFDL-files/", 
            "MPI-files/",
            "UKESM-files/",
            "IPSL-files/",
            "MRI-files/",
            "wget-mitos/",
          )

def parse_file(filename:str, type=0):
    vars = filename.split("_")
    if vars[0] in ['pr', 'tas', 'tasmax', 'tasmin']: type = 1

    if not type:
        model = vars[0]
        ssp = vars[3]
        variable = vars[4]
        start = vars[7]
        end = vars[8][:4]
        return model, ssp, variable, start, end

    model = "Observation"
    ssp = 'W5E5v1.0'
    variable = vars[0]
    years = vars[2].split("-")
    start = years[0][:4]
    end = years[1][:4]
    return model, ssp, variable, start, end

#******* WRITE EACH FILE INTO SORTED FILE LOCATIONS *************
LIMIT = 3
for folder in FOLDERS:

    source_path = 'isimip-files/' + folder

    for count, file in enumerate(listdir(source_path)):
        #if count == LIMIT: break

        #? extract metadata from file
        try: model, ssp, variable, start, end = parse_file(file)
        except: continue

        #? ADDED: skip if its GFDL AND in [ssp126, ssp370]
        if folder == FOLDERS[0] and ssp in ['ssp126', 'ssp370']: continue

        #? figure out desitnation path and filename
        dest_path = 'small-isimip-files/'+folder
        final_filename = '-'.join([model, ssp, variable, start, end]) + '.txt'

        #? load in this file, EXTRACT all 3652 2x2 cells
        try: ds = nc.Dataset(source_path+file, 'r')
        except: continue
        data = ds[variable][:, 95:97, 217:219] 

        #? reshape array to 2D array and store to file
        data_reshaped = data.reshape(data.shape[0], -1)
        print(f"Writing file: {file} ".ljust(90, '.'), end="")
        np.savetxt(dest_path+final_filename, data_reshaped)
        print("DONE")

    print(f"=============================== FOLDER {folder} FINISHED! ===============================\n")
