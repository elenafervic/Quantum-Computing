import cirq
from cirq.circuits import InsertStrategy
import tensorflow as tf

import numpy as np
from numpy import around, log2, isreal, all, trace, conj, outer
from numpy import matrix, eye, count_nonzero, around, sum, save

from math import factorial, sqrt, pi #I think this one is standard for python.
from cmath import exp

import scipy, sympy
from scipy import interpolate
from sympy import Symbol


import matplotlib.pyplot as plt
from matplotlib import gridspec

import gc, random, timeit
from timeit import default_timer as timer
from IPython.display import Markdown, display

def printmd(string):
    display(Markdown(string))
    
# Unitary operator rotating the two-qubit basis of the Message and Alice's entangled qubit;
# rotates the Bell state basis to the computational basis:
circuit.append([cirq.CNOT(qubit[0], qubit[1]), cirq.H(qubit[0])])
# But this time skip the measurement
# circuit.append(cirq.measure(qubit[0], qubit[1]))

# Use the same operations as before to recover the
# original quantum Message on Bob's entangled qubit.
circuit.append([cirq.CNOT(qubit[1], qubit[2]), cirq.CZ(qubit[0], qubit[2])])
