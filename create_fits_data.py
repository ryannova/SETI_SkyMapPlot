import healpy as hp
import numpy as np

FILE_NAME = "filled_obs_pixel_info"

data = np.loadtxt(FILE_NAME)
hp.write_map("data_nobs.fits", data[:,1])
hp.write_map("data_nobs_gaussian.fits", data[:,2])
hp.write_map("data_time.fits", data[:,3])
hp.write_map("data_time_gaussian.fits", data[:,4])
