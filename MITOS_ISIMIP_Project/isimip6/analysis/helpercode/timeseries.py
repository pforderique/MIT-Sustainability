import numpy as np
from os import listdir

from .nameparser import parse_small_file
from .changeunits import kelvin_to_fahrenheit
import matplotlib.pyplot as plt

FOLDERS = (
            "GFDL-files/", 
            # "MPI-files/",
            # "UKESM-files/",
            # "IPSL-files/",
            # "MRI-files/",
            # "wget-mitos/",
          )

def extract_per_year(model:str, variable:str, ssp='ALL', start='2015', end='2100', type='MAX'):
    '''
    INPUTS
        model    - gfdl, mri, etc. (NOT ALL)
        variable - pr, tas, etc.   (NOT ALL)
        ssp      - ssp126, ssp370, ..., default = ALL
        start    - 2015, 2021, .., default = 2015
        end      - 2020, 2030, ..., defualt = 2100
        type     - MAX or MIN, default = MAX

    OUTPUT:
        an array of MAX/MIN variable values from start to end year
    '''
    # print(model, variable, ssp, start, end, type)
    
    path = "C:/Users/fabri/OneDrive/Documents/ArcGIS/Projects/MITOS_ISIMIP_Project/isimip6/analysis/small-isimip-files/"+ model.upper()+"-files/"
    res = []

    for count, file in enumerate(listdir(path)):
        
        filemodel, filessp, filevariable, filestart, fileend = parse_small_file(file)

        #? FILERTERING HERE. 
        if ssp != 'ALL' and ssp != filessp: continue
        if variable != filevariable: continue
        # ignore start and end years for now... just get full century data
        
        #************? Do meaningful work here now for each file! **************
        loaded_arr = np.loadtxt(path+file)

        # process year by year 
        for row in range(0, len(loaded_arr) - 365, 365):
            # get max's of all 4 columns: maxes = numpy.amax(a,axis=1)
            if type == 'MAX': 
                yearly_max_or_min = np.max(loaded_arr[row:row+365, 0]) # second column = MIT
            elif type == "MIN":
                yearly_max_or_min = np.min(loaded_arr[row:row+365, 1])
            
            if variable == 'pr': res.append(yearly_max_or_min)
            else: res.append(kelvin_to_fahrenheit(yearly_max_or_min))

    return res

if __name__ == "__main__":
    VAR = 'tasmin'
    years = [year for year in range(2015, 2101)]
    data = extract_per_year('gfdl', VAR, 'ssp585', type='MIN')

    plt.plot(years, data, 'o-')
    plt.show()

