import netCDF4 as nc

FILE_PATH = "tasmax_day_GFDL-ESM2M_rcp85_r1i1p1_EWEMBI_landonly_20910101-20991231.nc"
MIT_COORDINATES = (42.3601, 71.0942)

#* load in the dataset 
ds = nc.Dataset(FILE_PATH, 'r')

#* A NetCDF file has three basic parts: metadata, dimensions and variables.
#* Variables contain both metadata and data

#* Printing the dataset gives us information about the variables contained in the file and their dimensions.
print(ds)

#* Each dimension is stored as a dimension class which contains pertinent information. 
#* Metadata for all dimensions can be access by looping through all available dimensions, like so.
# for dim in ds.dimensions.values():
#     print(dim)
#* Individual dimensions are accessed like so: ds.dimensions['x'].
# print(ds.dimensions['lon'])

#* ds.variables.values() for variables

print(ds['tasmaxAdjust'][0, 95:97, 217:219])
#* The actual precipitation data values are accessed by array indexing, and a numpy array is returned
# precips = ds['pr'][:]
#* Or a subset can be returned. The following code returns a 2D subset.
# precips = ds['pr'][0, 200:205, 200:205]
# precips = ds['pr']

# #* this is precips = ds['pr'][0, 95:97, 217:219] 
# data = ds['pr'][1:3, 95:97, 217:219] 
# print(data)

#* reshape array to 2D array so we can store in file
# data_reshaped = data.reshape(data.shape[0], -1)
# print(data_reshaped)

#* save it to custom file name
# np.savetxt("geekfile.txt", data_reshaped)

#* to get it back later: - dont forget to reshape back? or LEAVE it?
# loaded_arr = np.loadtxt("geekfile.txt")
# load_original_arr = loaded_arr.reshape(loaded_arr.shape[0], 2, 2)

# print(load_original_arr)