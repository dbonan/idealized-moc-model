def psi_na(pn, pa):
    """
    Description:
        Computes the meridional streamfunction for the North Atlantic with
        boundary conditions \psi = 0 at z = 0 and z = -H.
        
    Input:
        pn  :  vertical profile of density in the North Atlantic  [ kg m^{-3} ]
        pa  :  vertical profile of density in the Atlantic basin  [ kg m^{-3} ]
        
    Output:
        psi :  vertical profile of the streamfunction             [ m^{3} s^{-1} ]
    """
    import parameters as pm
    import numpy as np
    from vertical_grid import vertical_grid
    
    g     = pm.g
    fn    = pm.fn
    p0    = pm.p0
    hz    = pm.hz
    dz    = pm.dz
    zt, zw, nzt, nzw = vertical_grid(hz,dz)
    
    psi   = np.zeros(nzw)
    int_0 = np.zeros(nzw)
    
    for i in range(1, nzw):
        int_0[i] = int_0[i-1] + dz*g/(fn*p0) * (pn[i-1] - pa[i-1])

    int_1   = np.zeros(nzw)
    for i in range(1, nzw):
        int_1[i] = int_1[i-1] + dz*0.5 * (int_0[i] + int_0[i-1])

    d     = -int_1[-1]
    c     = d/hz
    psi   = (int_1 + c*zw + d)
    
    return psi