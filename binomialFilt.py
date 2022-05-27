from cmath import pi
import math
import numpy as np

from plotrefl import *

# Given N (number of sections), ZL (load impedance), Z0 (feedline impedance) design a binomial transformer

def binom_design(N, Z0, ZL):

    # The array Zn will contain Z1, Z2, ...., ZN, that is the characteristic impedance of each section
    # Consider as first element Z0, even if Z0 is the char. imp. of the feedline
    # The last element will be ZL

    Zn = [Z0]

    for k in range(0,N):

        nchoosek = math.comb(N, k)
        
        Zn_next = Zn[k]*(ZL/Z0)**(nchoosek/2**N)
        Zn.append(Zn_next)
    
    Zn.append(ZL)
    return Zn



