#Note that this code was obtained from chat gpt to diagonalise matrices.
# The original querie was "Hi Chat GPT, can you write me python code to diagonalise a matrix please?"
#I also searched for the following thing afterwards to incorporate symbolic mathematics "how would I implement algebraic variables into the matrix?", which led me to sympy.

import sympy as sp
import numpy as np

def diagonalize_matrix_symbolic(A):
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = A.diagonalize()
    
    return eigenvalues, eigenvectors

# Define symbolic variables
a, b, c, d = sp.symbols('a b c d')

# Create a matrix with symbolic variables
A = sp.Matrix([[a, b], [c, d]])

D, P = diagonalize_matrix_symbolic(A)

print("Original Matrix A:")
sp.pprint(A)
print("\nDiagonal Matrix D:")
sp.pprint(D)
print("\nEigenvector Matrix P:")
sp.pprint(P)
print("\nVerification (P * D * P^-1):")
sp.pprint(P * D * P.inv())
