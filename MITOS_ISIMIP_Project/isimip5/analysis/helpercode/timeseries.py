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
    
    path = r"C:/Users/fabri/OneDrive/Documents/ArcGIS/Projects/MITOS_ISIMIP_Project/isimip5/analysis/small-isimip5-files/"+ model.upper()+"-files/"
    res = []

    for count, file in enumerate(listdir(path)):
        
        filemodel, filessp, filevariable, filestart, fileend = parse_small_file(file)

        #! skip (for now) models that go over the 2100 year limit
        if int(filestart) > 2100: continue

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
    VAR = 'tasmax'
    # data = extract_per_year('gfdl', VAR, 'rcp85', type='MAX')
    # years = [year for year in range(2006, 2006+len(data))]

    data = extract_per_year('OBSERVATION', VAR, 'GSWP3')
    years = [year for year in range(1901, 1901+len(data))]

    plt.plot(years, data, 'o-')
    plt.show()

