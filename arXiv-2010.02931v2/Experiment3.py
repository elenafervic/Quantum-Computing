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

# Get two qubits and a circuit
qubit = [cirq.LineQubit(x) for x in range(2)]
circuit = cirq.Circuit()

# Add a Hadamard gate to make the initial state of qubit 0:
circuit.append([cirq.H(qubit[0])])

# Get a symbol
symbol = Symbol("t")
# Add a parameterized XPowGate to make the initial state of qubit 1:
circuit.append([cirq.XPowGate(exponent=symbol)(qubit[1])])

# Add three CNOT gates to make a SWAP gate:
circuit.append([cirq.CNOT(qubit[0], qubit[1]),
               cirq.CNOT(qubit[1], qubit[0]),
               cirq.CNOT(qubit[0], qubit[1])])

# Measure qubit 1 first, then measure qubit 0:
circuit.append(cirq.measure(qubit[1], key='q1'))
circuit.append(cirq.measure(qubit[0], key='q0'), strategy=InsertStrategy.NEW)

# Display the circuit:
printmd("\n**Cirq circuit:**")
print(circuit)

# Get a sweep over parameter values
sweep = cirq.Linspace(key=symbol.name, start=0.0, stop=1.0, length=3)

# Execute the circuit for all values in the sweep
sim = cirq.Simulator()
results = sim.run_sweep(circuit, sweep, repetitions=50)
printmd("\n**Results for t = 0:**")
print(results[0])
printmd("\n**Results for t = 1:**")
print(results[2])
printmd("\n**Results for t = 0.5:**")
print(results[1])
