'''
This file has already been run. Do not run again.
Here for archive only.
'''

from matplotlib import pyplot as plt
from .timeseries import extract_per_year

FOLDERS = (
            "GFDL-files/", 
            "MPI-files/",
            "UKESM-files/",
            "IPSL-files/",
            "MRI-files/",
            "OBSERVATION-files/",
          )

VARIABLES = ('pr', 'tas', 'tasmax', 'tasmin')
  
# MODEL = 'mpi'
# VAR = 'tasmax'
# SSP = 'ssp126'
# TYPE = 'MAX'

YEARS = [year for year in range(2015, 2101)]

def create_visuals():
    for FOLDER in FOLDERS:
        print("======= Starting folder:", FOLDER, "=======")

        #? determine what the SSPS are
        if FOLDER == "OBSERVATION-files/": SSPS = ('W5E5v1.0',)
        else: SSPS = ('ssp126','ssp370', 'ssp585')

        for VAR in VARIABLES:
            print("\t On variable:", VAR)

            #? determine the TYPE:
            if VAR == 'tasmin': TYPE = 'MIN'
            else: TYPE = 'MAX'

            for SSP in SSPS:
                print("\t\t On ssp:", SSP)
                
                model = FOLDER.split('-')[0] 
                fname = model + '-' + VAR + '-' + SSP
                SAVE_PATH = './visuals/' + model + '-visuals/' + fname
                
                # get this data array
                data = extract_per_year(model, VAR, SSP, TYPE)
                print(len(data))

                #? DIFFERENT YEARS FOR OBSERVATIONS
                if model == 'OBSERVATION':
                    YEARS = [yr for yr in range(1979, 2017)]
                plt.plot(YEARS[:len(data)], data, 'o-')

                # add titles and save figure in path
                plt.title(fname)
                plt.ylabel(VAR)
                plt.xlabel('YEARS')
                plt.savefig(SAVE_PATH+'.png')
                plt.clf()

# create_visuals()