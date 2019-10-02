import healpy as hp
import numpy as np
import matplotlib.pyplot as plt
#From Nonlinear Map
from pylab import *
from matplotlib.colors import LinearSegmentedColormap

class nlcmap(LinearSegmentedColormap):
    """A nonlinear colormap"""
    
    name = 'nlcmap'
    
    def __init__(self, cmap, levels):
        self.cmap = cmap
        # @MRR: Need to add N for backend
        self.N = cmap.N
        self.monochrome = self.cmap.monochrome
        self.levels = asarray(levels, dtype='float64')
        self._x = self.levels / self.levels.max()
        self._y = linspace(0.0, 1.0, len(self.levels))
    
    #@MRR Need to add **kw for 'bytes'
    def __call__(self, xi, alpha=1.0, **kw):
        """docstring for fname"""
        # @MRR: Appears broken? 
        # It appears something's wrong with the
        # dimensionality of a calculation intermediate
        #yi = stineman_interp(xi, self._x, self._y)
        yi = interp(xi, self._x, self._y)
        return self.cmap(yi, alpha)
##END
IMAGE_OUTPUT = "images/"
COLOR_MAP = "Wistia"
IMAGE = "skymap_source.png"
FITS_FILES = ["data_time.fits", "data_time_gaussian.fits", "data_nobs.fits", "data_nobs_gaussian.fits"]
plt.rcParams.update({'font.size': 22})

map_array = []
for filename in FITS_FILES:
    m = hp.read_map(filename)
    maps = hp.visufunc.cartview(m, return_projected_map=True, nest=True)
    map_array.append(np.array(maps))
img = plt.imread(IMAGE)

index = 0
for filename in FITS_FILES:
    plt.figure(figsize=(30,20))
    plt.imshow(img)
    plt.imshow(map_array[index], cmap=COLOR_MAP, interpolation='nearest', alpha=0.5, extent=(-0.5, img.shape[1]-0.5, img.shape[0]-0.5,-0.5))
    plt.colorbar(orientation="horizontal")
    newname = filename[:-5]
    plt.savefig(IMAGE_OUTPUT + "img_" + COLOR_MAP + '_' + newname + ".png")
    index += 1
