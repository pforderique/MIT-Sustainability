import numpy as np
from os import listdir 
from matplotlib import pyplot as plt
from helpercode.timeseries import extract_per_year

FOLDERS = (
            "GFDL-files/", 
            "MPI-files/",
            "UKESM-files/",
            "IPSL-files/",
            "MRI-files/",
            "OBSERVATION-files/",
          )
  
MODEL = 'gfdl'
VAR = 'pr'
SSP = 'ssp370'
TYPE = 'MAX'

years = [year for year in range(2015, 2101)]
data = extract_per_year(MODEL, VAR, SSP, TYPE)
# print(data)

# print(np.quantile(data, 0.1))

# plt.plot(years, data, 'o-')

# plt.clf()
# data = extract_per_year('observation', VAR, SSP, TYPE)
print(np.quantile(data, 0.99))
plt.plot(years, data, 'o-')

plt.show()
# print(data)