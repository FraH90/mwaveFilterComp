from binomialFilt import *
import matplotlib.pyplot as plt

# Let's set feedline and load impedance
Z0 = 50
ZL = 75

# Set central frequency f0 at 2.4 GHz, light speed in vacuum, central wavelength (at f0), physical length of each section
f0 = 2.4e9
c = 3e8
lambda0 = c/f0
sect_length = lambda0/4



# frequency sweep parameters
fmin = 0.2e9
fmax = 4.6e9
nstep = 1000


# Let's set parameters for the number of section variable
Nmin = 1
Nmax = 8
Nstep = 2



i = Nmin

while i <= Nmax:
    # Design a binomial transformer with 'i' sections, that adapts from Z0 = 50ohm to ZL = 75ohm
    Zn = binom_design(i, Z0, ZL)

    print(Zn)
    
    # Let's do a frequency sweep and get the reflection coefficient at sample frequencies in the range fmin-fmax
    gammafreqsweep = refl_coeff_fsweep(Zn, f0, fmin, fmax, nstep)

    # plot reflection coefficient as function of frequency
    plt.plot(gammafreqsweep[0], gammafreqsweep[1], label=f'N = {i}')
    
    i += Nstep
    
plt.xlabel('f [GHz]')
plt.ylabel('|| \u0393 ||')
plt.legend()

plt.axhline(y = 0.05, color = 'r', linestyle = ':')

plt.show()