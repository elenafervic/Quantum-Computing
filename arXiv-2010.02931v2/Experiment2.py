# Get two qubits and a circuit
qubit = [cirq.LineQubit(x) for x in range(2)]
circuit = cirq.Circuit()

# Add a Hadamard gate to qubit 0, then a CNOT gate from qubit 0 to qubit 1:
circuit.append([cirq.H(qubit[0]), 
             cirq.CNOT(qubit[0], qubit[1])])

# Run a simple simulation that extracts the actual final states
sim = cirq.Simulator()
result = sim.simulate(circuit)
printmd("\n**Bloch Sphere of the qubit 0 in the final state:**")
state = cirq.bloch_vector_from_state_vector(result.final_state,0)
print("x: ", around(state[0], 4), " y: ", around(state[1], 4),
      " z: ", around(state[2], 4))
printmd("\n**Bloch Sphere of the qubit 1 in the final state:**")
state = cirq.bloch_vector_from_state_vector(result.final_state,1)
print("x: ", around(state[0], 4), " y: ", around(state[1], 4),
      " z: ", around(state[2], 4))

# Add a measurement at the end of the circuit: 
circuit.append(cirq.measure(*qubit, key="Final state"))

# Display the circuit:
printmd("\n**Cirq circuit:**")
print(circuit)

# Invoke the Cirq quantum simulator to execute the circuit:
simulator = cirq.Simulator()

# Simulate the circuit several times:
result = simulator.run(circuit, repetitions=10)

# Print the results:
printmd("\n**Results:**")
print(result)
