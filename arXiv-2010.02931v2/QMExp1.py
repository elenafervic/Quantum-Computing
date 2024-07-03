# Get a qubit and a circuit
qbit = cirq.LineQubit(0)
circuit = cirq.Circuit()

# Add an X gate: acts like the Pauli Matrix sigma_x
circuit.append(cirq.X(qbit))

# Run a simple simulation that extracts the wavefunction of this state
sim = cirq.Simulator()
result = sim.simulate(circuit)
printmd("\n**Bloch Sphere of the qubit in the final state:**")
state = cirq.bloch_vector_from_state_vector(result.final_state,0)
print("x: ", around(state[0], 4), " y: ", around(state[1], 4),
      " z: ", around(state[2], 4))

# Add a measurement at the end of the circuit: 
circuit.append(cirq.measure(qbit, key="Final state"))

# Display the circuit:
printmd("\n**Cirq circuit:**")
print(circuit)

# Invoke the Cirq quantum simulator to execute the circuit:
simulator = cirq.Simulator()

# Simulate the circuit several times:
result = simulator.run(circuit, repetitions=10)

# Print the results:
printmd("\n**Results of 10 trials:**")
print(result)
