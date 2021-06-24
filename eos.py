def eos(t,s):
    """
    Description:
        Computes potential density using a linear equation of state.
        
    Input:
        t   : temperature                              [ °C ]
        s   : salinity                                 [ g/kg ]
        
    Output:
        p   : potential density                        [ kg/m^3 ]
    """
    import parameters as pm
    
    p0 = pm.p0
    t0 = pm.t0
    s0 = pm.s0
    a  = pm.a
    b  = pm.b
    
    p = p0 * (1 - a*(t-t0) + b*(s-s0))
    
    return p