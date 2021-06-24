import numpy as np

def vertical_grid(h,dz):
    """
    Description:
        Computes vertical grid for column model.
        
    Input:
        h   : depth of ocean                              [ m ]
        dz  : size of grid box                            [ m ]
        
    Output:
        zt  : vertical grid for temperature/salinity      [ m ]
        zw  : vertical grid for velocity                  [ m ]
        nzt : size of temperature/salinity vertical grid
        nzw : size of velocity vertical grid 
    """
    nzt = int(h/dz)
    nzw = nzt + 1
    zt  = np.arange(-h, 0, dz) + dz/2
    zw  = np.arange(-h, dz, dz)
    return zt, zw, nzt, nzw