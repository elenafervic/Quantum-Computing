# Define three qubits: msg = qubit[0], qalice = qubit[1], qbob = qubit[2]
qubit=[0]*(3)
qubit[0] = cirq.NamedQubit('msg')
qubit[1] = cirq.NamedQubit('qalice')
qubit[2] = cirq.NamedQubit('qbob')

circuit = cirq.Circuit()
# Create a Bell state entangled pair to be shared between Alice and Bob.
circuit.append([cirq.H(qubit[1]), cirq.CNOT(qubit[1], qubit[2])])

# Creates a random state for the Message.
ranX = random.random()
ranY = random.random()
circuit.append([cirq.X(qubit[0])**ranX, cirq.Y(qubit[0])**ranY])

# Unitary operator rotating the two-qubit basis of the Message and Alice's entangled qubit;
# rotates the Bell state basis to the computational basis:
circuit.append([cirq.CNOT(qubit[0], qubit[1]), cirq.H(qubit[0])])
# Combining now with a measurment in the computational basis,
# we effectively have projected this two-qubit state onto one of the four states of
# the Bell state basis:
circuit.append(cirq.measure(qubit[0], qubit[1]))

# Use the two classical bits from the Bell measurement to recover the
# original quantum Message on Bob's entangled qubit.
circuit.append([cirq.CNOT(qubit[1], qubit[2]), cirq.CZ(qubit[0], qubit[2])])

printmd("\n**Cirq circuit:**")
print(circuit)

sim = cirq.Simulator()

# Run a simple simulation that applies the random X and Y gates that
# create our message.
q0 = cirq.LineQubit(0)
message = sim.simulate(cirq.Circuit([cirq.X(q0)**ranX, cirq.Y(q0)**ranY]))

printmd("\n**Bloch Sphere of the Message qubit in the initial state:**")
expected = cirq.bloch_vector_from_state_vector(message.final_state,0)
print("x: ", around(expected[0], 4), " y: ", around(expected[1], 4),
      " z: ", around(expected[2], 4))

# Records the final state of the simulation.
final_results = sim.simulate(circuit)

printmd("\n**Bloch Sphere of Bob's qubit in the final state:**")
teleported = cirq.bloch_vector_from_state_vector(
    final_results.final_state, 2)
print("x: ", around(teleported[0], 4), " y: ",
    around(teleported[1], 4), " z: ", around(teleported[2], 4))

printmd("\n**Bloch Sphere of the Message qubit in the final state:**")
message_final = cirq.bloch_vector_from_state_vector(
    final_results.final_state, 0)
print("x: ", around(message_final[0], 4), " y: ",
    around(message_final[1], 4), " z: ", around(message_final[2], 4))
