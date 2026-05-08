# Bob: Receiver -> chooses bases, measures qubits

import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

class Bob:
    def __init__(self):
        self.bases = []
        self.results = []
    
    def choose_bases(self, n):
        """Bob randomly chooses measurement bases"""
        self.bases = [random.choice(['+', 'x']) for _ in range(n)]
        return self.bases
    
    def measure_qubit(self, circuit, basis):
        """
        Measure qubit in given basis.
        For x-basis, apply H gate before measurement.
        """
        qc = circuit.copy()
        
        # Transform basis if measuring in x
        if basis == 'x':
            qc.h(0)
        
        # Measure
        qc.measure(0, 0)
        
        # NEW QISKIT 1.0+ METHOD
        simulator = Aer.get_backend('qasm_simulator')
        
        # Transpile the circuit for the backend
        compiled_circuit = transpile(qc, simulator)
        
        # Run the simulation
        job = simulator.run(compiled_circuit, shots=1)
        result = job.result()
        counts = result.get_counts()
        
        return int(list(counts.keys())[0])
    
    def measure_all(self, circuits):
        """Measure all received qubits"""
        self.results = []
        
        for circuit, basis in zip(circuits, self.bases):
            result = self.measure_qubit(circuit, basis)
            self.results.append(result)
        
        return self.results
    
    def get_data(self):
        """Return all Bob's data"""
        return {
            'bases': self.bases,
            'results': self.results
        }