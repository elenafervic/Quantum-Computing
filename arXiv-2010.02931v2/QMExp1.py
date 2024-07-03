#--------------------------------------------Imports-----------------------------------------------------------
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

#-------------------------------------------Start Actual Code--------------------------------------------------

# Get a qubit and a circuit
qbit = cirq.LineQubit(0)#Initialise qubit in state 0.
circuit = cirq.Circuit()#Initialise the cirquit (empty for now)

# Add an X gate: acts like the Pauli Matrix sigma_x
circuit.append(cirq.X(qbit))

# Run a simple simulation that extracts the wavefunction of this state
sim = cirq.Simulator()
result = sim.simulate(circuit)
#printmd("\n**Bloch Sphere of the qubit in the final state:**")# This was the original spelling, but it looked weird on vs code.
print("\n**Bloch Sphere of the qubit in the final state:**")
state = cirq.bloch_vector_from_state_vector(result.final_state_vector,0)
print("x: ", around(state[0], 4), " y: ", around(state[1], 4),
      " z: ", around(state[2], 4))

# Add a measurement at the end of the circuit: 
circuit.append(cirq.measure(qbit, key="Final state"))

# Display the circuit:
#printmd("\n**Cirq circuit:**")# This was the original spelling, but it looked weird on vs code.
print(circuit)

# Invoke the Cirq quantum simulator to execute the circuit:
simulator = cirq.Simulator()

# Simulate the circuit several times:
result = simulator.run(circuit, repetitions=10)

# Print the results:

#printmd("\n**Results of 10 trials:**")# This was the original spelling, but it looked weird on vs code.
print("\n**Results of 10 trials:**")
print(result)
