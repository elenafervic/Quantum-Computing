# Unitary operator rotating the two-qubit basis of the Message and Alice's entangled qubit;
# rotates the Bell state basis to the computational basis:
circuit.append([cirq.CNOT(qubit[0], qubit[1]), cirq.H(qubit[0])])
# But this time skip the measurement
# circuit.append(cirq.measure(qubit[0], qubit[1]))

# Use the same operations as before to recover the
# original quantum Message on Bob's entangled qubit.
circuit.append([cirq.CNOT(qubit[1], qubit[2]), cirq.CZ(qubit[0], qubit[2])])
