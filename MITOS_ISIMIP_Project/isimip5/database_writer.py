import netCDF4 as nc
import numpy as np
from os import listdir

print("++++++++\nTRANSFER STARTED\n++++++++\n")

SCALE = 86400*0.03937 # to convert mm/sec -> in/day

FOLDERS = (
            # "GFDL-files/", 
            # "IPSL-files/",
            # 'HadGEM2-files/',
            # 'MIROC5-files/',
            'GSWP3-files/',
          )

def parse_file(filename:str):
    vars = filename.split("_")

    if 'gswp3' in filename:
        model = "OBSERVATION"
        ssp = 'gswp3'
        variable = vars[0]
        start = vars[2]
        end = vars[3][:4]

    else:
        model = vars[2]
        ssp = vars[3]
        variable = vars[0]
        timing = vars[7].split('-')
        start = timing[0][:4]
        end = timing[1][:4]

    return model, ssp, variable, start, end

#******* WRITE EACH FILE INTO SORTED FILE LOCATIONS *************
for folder in FOLDERS:

    source_path = 'isimip5-files/' + folder

    for count, file in enumerate(listdir(source_path)):

        #? extract metadata from file
        try: model, ssp, variable, start, end = parse_file(file)
        except: 
            print("INFO COULD NOT BE EXTRACTED FROM: ", file, "---------- SKIPPED.")
            continue

        #? figure out desitnation path and filename
        dest_path = 'small-isimip5-files/'+folder
        final_filename = '-'.join([model, ssp, variable, start, end]) + '.txt'

        #? load in this file, EXTRACT all 3652 2x2 cells
        try: 
            ds = nc.Dataset(source_path+file, 'r')
        except: 
            print("Could not load file: ", file, "----------- SKIPPED.")
            continue
        if model != 'OBSERVATION': data = ds[variable+"Adjust"][:, 95:97, 217:219] 
        else: data = ds[variable][:, 95:97, 217:219] 

        #? scale the pr data 
        if variable == "pr": data *= SCALE

        #? reshape array to 2D array and store to file
        data_reshaped = data.reshape(data.shape[0], -1)
        print(f"Writing file: {file} ".ljust(90, '.'), end="")
        np.savetxt(dest_path+final_filename, data_reshaped)
        print("DONE")

    print(f"=============================== FOLDER {folder} FINISHED! ===============================\n")
