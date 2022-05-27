# Microwave transformer comparison

## Requirements

- A full working python3 installation
- Matplotlib
- Numpy


## Intro
This software shows comparison between two widely used impedance transformer at microwave frequencies: the binomial transformer, and the Chebyshev transformer (which uses Chebyshev polinomials as a basis for generating the reflection coefficients/step impedances of each section).

For the binomial transformer, the first script 00-binomialFilt_N4.py generates the step impedances required to adapt a Z0 = 50ohm feedline to a ZL = 75ohm load, using N=4 sections (the number of sections can be changed in the code).
The magnitude of the reflection coefficient at the feedline is then plotted against frequency (for info on how the script execute this job, read later).

The 01-binomialFilt_Nvar.py script instead generates step impedances for various N (default: N= 1, 3, 5, 7) and then it plots the magnitude of the reflection coefficient at the input of each transformer versus frequency.
Here we can see that by increasing the number of section that constitute the transformer, we increase the bandwidth (defined as the range of frequencies in which the absolute value of the reflection coefficient stay under a certain value, gamma_m).

Finally the 02-binom-cheb-N3-comparison.py script make a comparison between a binomial adapter and a Chebyshev adapter, both with N=3.
We see that the Chebyshev adapter has an higher bandwidth than the binomial. The tradeoff is that the Chebyshev adapter has a ripple in the bandwidth, but this can be minimized by setting up a low value for gamma_m.
The advantage is that by using a Chebyshev transformer we have an higher bandwidth, by using the same number of sections of a binomial.


## How it works

The code that compute the magnitude of the reflection coefficients and plots Γ(f) is in plotrefl.py.

First we find the characteristic impedance of each section, and the length that it must have for being a lambda/4 section at the central frequency f0 (by default f0=2.4GHz).

After that, we compute the ABCD matrix (at the sample frequency f) of each section that make up the transformer by using the known formula for the ABCD matrix of a transmission line.

Then we find the complessive ABCD matrix of the transformer by computing the matrix product of each ABCD of each section, in sequence ( ABCD_Z1 \* ABCD_Z2 \* ..... \* ABCD_ZN ).

Finally we compute the Zin at the input of the feedline by using Zin = (A\*ZL + B)/(C\*ZL + D), and then we transform Zin in its relative reflection coefficient (gamma = (Zin-Z0)/(Zin+Z0)).

This computes the reflection coefficient at a single frequency f. In order for us to draw a plot Γ(f), we need to iterate this process at each sample frequency. This is simply done in a for loop by calling the function multiline_reflection_coeff_abs(Zn, f0, f) at the frequency that is of our interest).


## Code execution

The executable files are:

- 00-binomialFilt_N4.py
- 01-binomialFilt_Nvar.py
- 02-binom-cheb-N3-comparison.py

Simply double click them, or execute them in VSCode (with the proper setup).
