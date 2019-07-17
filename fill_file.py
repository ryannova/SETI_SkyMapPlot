#imports
import numpy as np

#constants
FILE_NAME = "obs_pixel_info"

#functions
def fill_file(rawdata):
    fixed_data = []
    current_index = 0
    max_index = rawdata[-1][0]
    for i in rawdata:
        while current_index != i[0]:
            fixed_data.append([current_index, 0, 0, 0, 0])
            current_index += 1
        fixed_data.append(i)
        current_index += 1
    return fixed_data

#main
data = np.loadtxt(FILE_NAME)
filled_data = fill_file(data)
np.savetxt("filled_" + FILE_NAME, filled_data)

