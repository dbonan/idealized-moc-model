import numpy as np

def vertical_grid(dz,h):

    nzt = int(h/dz)
    nzw = nzt + 1
    zt  = np.arange(-h, 0, dz) + dz/2
    zw  = np.arange(-h, dz, dz)
    return zt, zw, nzt, nzw
