# This design a chebyshev transformer with max. reflection coefficient 0.05
# ZL/Z0 must be 1.5
def cheb_design_N3_rhom005():
    Zn = [50]
    Zn.append(Zn[0]*1.1029)
    Zn.append(Zn[0]*1.2247)
    Zn.append(Zn[0]*1.3601)
    Zn.append(75)

    return Zn


# This design a chebyshev transformer with max. reflection coefficient 0.2
# ZL/Z0 must be 1.5
def cheb_design_N3_rhom02():
    Zn = [50]
    Zn.append(Zn[0]*1.2247)
    Zn.append(Zn[0]*1.2247)
    Zn.append(Zn[0]*1.2247)
    Zn.append(75)

    return Zn

