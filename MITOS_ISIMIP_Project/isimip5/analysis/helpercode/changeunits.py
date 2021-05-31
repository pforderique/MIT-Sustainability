'''
DO NOT RUN THIS FILE AGAIN
TASK HAS ALREADY BEEN COMPLETED!

(In the event that you do, however, simply change line 40 to divide instead of multiply and run again.)
'''

import numpy as np
from os import listdir 
from .nameparser import parse_small_file


def kelvin_to_fahrenheit(kelvin):
    return (9.0/5)*(kelvin - 273) + 32

if __name__ == "__main__":

    SCALE = 86400*0.03937 # to convert mm/sec -> in/day

    FOLDERS = (
            "GFDL-files/", 
            "IPSL-files/",
            # 'HadGEM2-files/',
            # 'MIROC5-files/',
            )

    for folder in FOLDERS:
        path = "small-isimip5-files/" + folder

        for count, file in enumerate(listdir(path)):
            
            model, ssp, variable, start_year, end_year = parse_small_file(filename=file)
            print(model, ssp, variable, start_year, end_year)


            #? INSERT ANY FILERTERING HERE. 
            #? Ex: if variable == 'pr': continue (skip)
            if variable != 'pr': continue
            
            #************? Do meaningful work here now for each file! **************
            try: 
                loaded_arr = np.loadtxt(path+file)
                loaded_arr *= SCALE
            except:
                print("error loading:", file)
                continue
            
            try:
                np.savetxt(path+file, loaded_arr)
            except:
                print("Error writing to file:", file)

