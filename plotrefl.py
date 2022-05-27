from cmath import pi
import math
import numpy as np


def multiline_reflection_coeff_abs(Zn, f0, f):

    j = 1j

    # first, compute the entire ABCD of the system (Z1, Z2, ... ZN; Z0 and ZL are excluded)
    # by evaluating every single ABCD matrix of each line, and by evaluating the matrix product 
    # of each ABCD matrix. This is done at a specific frequency f

    # The ABCD matrix in fact will be a function of theta, which in turn it's a function of f.

    # theta = beta*length = (2pi/lambda)*(lambda0/4) = (pi/2) * (f/f0)
    # Here f is a variable, it's not the central frequency f0
    theta = (pi/2) * (f/f0)

    # The number of section is found from Zn by not considering Z0 and ZL, which are contained in Zn
    # Also, we explicitely define the feedline and load impedance
    N = len(Zn) - 2
    Z0 = Zn[0]
    ZL = Zn[-1]


    # Lets find the ABCD matrix of line Z1, Z2, ... ZN and then multiply all the ABCD matrix together

    ABCD_tot = np.matrix([[1, 0], [0, 1]])

    for k in range(1, N+1):
        # Explicitly define the characteristic impedance of the k-th section
        Zk = Zn[k]
        Yk = 1/Zk

        ABCD_element = [ [ math.cos(theta), j*Zk*math.sin(theta)], [j*Yk*math.sin(theta), math.cos(theta)] ]
        ABCD_element = np.matrix(ABCD_element)
        ABCD_tot = np.matmul(ABCD_tot, ABCD_element)

    
    # Evaluate the Zin in the port 1 of the multiline transformer, when ZL is attached to the end (using Zin = (A*ZL + B)/(C*ZL+D))

    A = ABCD_tot[0, 0] 
    B = ABCD_tot[0, 1]
    C = ABCD_tot[1, 0]
    D = ABCD_tot[1, 1]

    Zin = (A*ZL + B) / (C*ZL + D)

    # Evaluate the reflection coefficient from the Zin, return its absolute value
    gammain = (Zin-Z0)/(Zin+Z0)
    gammain_abs = abs(gammain)
    return gammain_abs



def refl_coeff_fsweep(Zn, f0, fmin, fmax, N_fstep):
    
    # N_fstep is an integer; it's the number of intervals in which we divide the frequency interval fmin : fmax
    # fstep is the increment to the next frequency at which we're sampling gammain_abs

    fstep = (fmax-fmin)/N_fstep

    # gammain_abs_freqsweep is a matrix that contain in the first coloumn the frequency at which gammain_abs has been evaluated, 
    # and in the second coloumn gammain_abs(freq). Let's initizalize it as an empty 0x2 matrix
    # Remember that the first coloumn is indexed as [0], while the second coloumn as [1]
    gammain_abs_freqsweep = [[], []]

    for i in range(0, N_fstep+1):
        # frequency at which we'll evaluate gammain_abs
        freq = fmin + i*fstep

        gammain_abs_freqsweep[0].append(freq)
        gammain_abs_freqsweep[1].append(multiline_reflection_coeff_abs(Zn, f0, freq))

    return gammain_abs_freqsweep

