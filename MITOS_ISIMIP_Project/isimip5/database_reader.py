import numpy as np

TXT_FILE =  'small-isimip-files\GFDL-files\gfdl-esm4-ssp126-pr-2021-2030.txt'

#* to get it back later: - dont forget to reshape back? or LEAVE it?
loaded_arr = np.loadtxt(TXT_FILE)
print(loaded_arr.shape)
load_original_arr = loaded_arr.reshape(loaded_arr.shape[0], 2, 2)

print(load_original_arr.shape)