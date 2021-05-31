def parse_file(filename:str):
    '''
    INPUTS:
        filename: a string representing file name like:
            > ukesm1-0-ll_r1i1p1f2_w5e5_ssp126_pr_global_daily_2051_2060.nc (type 0)
            > pr_W5E5v1.0_19790101-19801231.nc (type 1)

        type: 0 or 1 represents how to parse file
            > type 0: parse normally for files in folders "GFDL, MPI, MRI, etc"
            > type 1: parse filename from the script

    RETURNS <tuple of str>:
        model      : (GFDL, MPI, etc),
        ssp        : (ssp126, ssp370, etc.)
        variable   : (pr, tas, etc),  
        start year : (ex: 2011),
        end year   : (ex: 2020)
    '''

    vars = filename.split("_")

    if 'gswp3' in filename:
        model = "OBSERVATION"
        ssp = 'gswp3-ewembi'
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

def parse_small_file(filename:str):
    vars = filename.split("-")
    model = vars[0]
    if model == 'OBSERVATION':
        ssp = "GSWP3"
        variable = vars[2]
        start = vars[3]
        end = vars[4][:4]
    elif model == "GFDL" or model == "HadGEM2":
        ssp = vars[2]
        variable = vars[3]
        start = vars[4]
        end = vars[5][:4]
    elif model == "MIROC5":
        ssp = vars[1]
        variable = vars[2]
        start = vars[3]
        end = vars[4][:4]
    else:
        ssp = vars[3]
        variable = vars[4]
        start = vars[5]
        end = vars[6][:4]
    return model, ssp, variable, start, end

if __name__ == "__main__":
    print(parse_file("tasmax_day_GFDL-ESM2M_rcp85_r1i1p1_EWEMBI_landonly_20910101-20991231.nc"))
    print(parse_small_file("GFDL-ESM2M-rcp85-pr-2006-2010.txt"))
    print(parse_small_file("IPSL-CM5A-LR-rcp85-pr-2006-2010.txt"))
    print(parse_small_file("HadGEM2-ES-rcp85-pr-2021-2030.txt"))
    print(parse_small_file("MIROC5-rcp85-pr-2006-2010.txt"))
    print(parse_file("pr_gswp3-ewembi_1991_2000.nc"))