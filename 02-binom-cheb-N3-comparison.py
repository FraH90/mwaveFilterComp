import numpy
from cheb import *
from binomialFilt import *
from plotrefl import *

import matplotlib.pyplot as plt

# Set central frequency f0 at 2.4 GHz, light speed in vacuum, central wavelength (at f0), physical length of each section
f0 = 2.4e9
c = 3e8
lambda0 = c/f0
sect_length = lambda0/4



# frequency sweep parameters
fmin = 0.2e9
fmax = 4.6e9
nstep = 1000


Zn_binom = binom_design(3, 50, 75)
Zn_cheb_rhom005 = cheb_design_N3_rhom005()

print("Zn binomiale N=3: \n", Zn_binom, "\n")
print("Zn Chebyshev N=3, rhom = 0.05 : \n", Zn_cheb_rhom005, "\n")


# Let's do a frequency sweep and get the reflection coefficient at sample frequencies in the range fmin-fmax
gammafreqsweep_cheb = refl_coeff_fsweep(Zn_cheb_rhom005, f0, fmin, fmax, nstep)

# plot reflection coefficient as function of frequency
plt.plot(gammafreqsweep_cheb[0], gammafreqsweep_cheb[1])


# Let's do the same thing for the binomial adapter
gammafreqsweep_binom = refl_coeff_fsweep(Zn_binom, f0, fmin, fmax, nstep)
plt.plot(gammafreqsweep_binom[0], gammafreqsweep_binom[1])


# Let's find bandwidth of both
# bandwidth_cheb = numpy.interp(0.025, gammafreqsweep_cheb[1], gammafreqsweep_cheb[0]) / 1e9
# print(bandwidth_cheb)

plt.axhline(y = 0.05, color = 'r', linestyle = ':')

plt.show()



# Se definiamo la banda a rhom = 0.05 sia per il binomiale che per chebyshev, vediamo che chebyshev ha banda
# molto piu estesa del binomiale