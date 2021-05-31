'''
Sorts the file data into 4 excel sheets

This code ran successfully
'''

from matplotlib import pyplot as plt
from helpercode.timeseries import extract_per_year
import pandas as pd

FOLDERS = (
            "GFDL-files/", 
            "MPI-files/",
            "UKESM-files/",
            "IPSL-files/",
            "MRI-files/",
            "OBSERVATION-files/",
          )

VARIABLES = ('pr', 'tas', 'tasmax', 'tasmin')

YEARS = [year for year in range(2015, 2101)]

pr_sheets = {'ssp126':-1, 'ssp370':-1, 'ssp585':-1, 'W5E5v1.0':-1}
tas_sheets = {'ssp126':-1, 'ssp370':-1, 'ssp585':-1, 'W5E5v1.0':-1}
tasmax_sheets = {'ssp126':-1, 'ssp370':-1, 'ssp585':-1, 'W5E5v1.0':-1}
tasmin_sheets = {'ssp126':-1, 'ssp370':-1, 'ssp585':-1, 'W5E5v1.0':-1}
workbooks = [pr_sheets, tas_sheets, tasmax_sheets, tasmin_sheets]

def add_data(model, var, ssp, data):
    
    # select the correct sheets
    if var == 'pr': sheets = pr_sheets
    elif var == 'tas': sheets = tas_sheets
    elif var == 'tasmax': sheets = tasmax_sheets
    elif var == 'tasmin': sheets = tasmin_sheets
    else: raise Exception('var not known.')

    # create one if DNE
    if type(sheets[ssp]) == int: 
        if model == 'OBSERVATION': YEARS = [yr for yr in range(1979, 2017)]
        else: YEARS =  [year for year in range(2015, 2101)]
        sheets[ssp] = pd.DataFrame({'YEARS':YEARS})
        
    # add in data to this ssp sheet
    sheets[ssp][model] = pd.Series(data)

def create_sheets():
    for FOLDER in FOLDERS:
        print("======= Starting folder:", FOLDER, "=======")

        #? determine what the S
        if FOLDER == "OBSERVATION-files/": SSPS = ('W5E5v1.0',)
        else: SSPS = ('ssp126','ssp370', 'ssp585')

        for VAR in VARIABLES:

            #? determine the TYPE:
            if VAR == 'tasmin': TYPE = 'MIN'
            else: TYPE = 'MAX'

            for SSP in SSPS:

                model = FOLDER.split('-')[0] 
                fname = model + '-' + VAR + '-' + SSP
                SAVE_PATH = './visuals/' + model + '-visuals/' + fname
                
                # get this data array
                data = extract_per_year(model, VAR, SSP, TYPE)

                #? DIFFERENT YEARS FOR OBSERVATIONS
                if model == 'OBSERVATION': YEARS = [yr for yr in range(1979, 2017)]

                print(f">>> model {model}, var {VAR}, ssp {SSP}, data size: {len(data)}")
                add_data(model, VAR, SSP, data)

def write_var_to_excel(sheets:dict):
    filename = './excelsheets/'

    if sheets is pr_sheets: filename += 'pr_data.xlsx'
    elif sheets is tas_sheets: filename += 'tas_data.xlsx'
    elif sheets is tasmax_sheets: filename += 'tasmax_data.xlsx'
    else: filename += 'tasmin_data.xlsx' # sheets is tasmin_sheets

    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    # write each dataframe to a different worksheet
    for ssp in sheets:
        sheets[ssp].to_excel(writer, sheet_name=ssp)

    writer.save()

def write_sheets_to_excel():
    for workbook in workbooks:
        write_var_to_excel(workbook)
    
create_sheets()
write_sheets_to_excel()
