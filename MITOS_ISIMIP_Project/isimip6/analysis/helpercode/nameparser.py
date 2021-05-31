def parse_file(filename:str, type=0):
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

def parse_small_file(filename:str):
    '''
    INPUTS:
        filename: a string representing file name like:
            > gfdl-esm4-ssp126-pr-2051-2060.txt
            > Observation-W5E5v1.0-pr-1981-1990.txt

    RETURNS <tuple of str>:
        model      : (GFDL, MPI, etc),
        ssp        : (ssp126, ssp370, etc.)
        variable   : (pr, tas, etc),  
        start year : (ex: 2011),
        end year   : (ex: 2020)
    '''
    vars = filename.split("-")
    return vars[0], vars[-4], vars[-3], vars[-2], vars[-1][:4]

if __name__ == "__main__":
    print(parse_file("ukesm1-0-ll_r1i1p1f2_w5e5_ssp126_pr_global_daily_2051_2060.nc"))
    print(parse_file("pr_W5E5v1.0_19790101-19801231.nc", 1))
    # model, ssp, variable, start, end = parse_file("ukesm1-0-ll_r1i1p1f2_w5e5_ssp126_pr_global_daily_2051_2060.nc")
    # final_filename = '-'.join([model, ssp, variable, start, end]) + '.txt'
    # print(final_filename)
    print(parse_small_file("gfdl-esm4-ssp126-pr-2051-2060.txt"))
    print(parse_small_file('Observation-W5E5v1.0-pr-1979-1980.txt'))

