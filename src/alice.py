# Alice: Sender -> generates bits, chooses bases, encodes qubits

import random
from qiskit import QuantumCircuit

class Alice:
    def __init__(self):
        self.bits = []
        self.bases = []
        self.states = []
        self.circuits = []
    
    def generate_bits(self, n):
        """Generate random classical bits (0 or 1)"""
        self.bits = [random.randint(0, 1) for _ in range(n)]
        return self.bits
    
    def generate_bases(self, n):
        """Generate random bases (+ or x)"""
        self.bases = [random.choice(['+', 'x']) for _ in range(n)]
        return self.bases
    
    def encode_bit(self, bit, basis):
        """
        Encode one bit into quantum state.
        
        Cases:
        bit=0, basis='+' -> |0>  (no gates)
        bit=1, basis='+' -> |1>  (X gate)
        bit=0, basis='x' -> |+>  (H gate)
        bit=1, basis='x' -> |->  (X then H)
        """
        qc = QuantumCircuit(1, 1)
        
        # Apply X gate for bit 1
        if bit == 1:
            qc.x(0)
        
        # Apply H gate for x basis
        if basis == 'x':
            qc.h(0)
        
        # Record state for display
        if bit == 0 and basis == '+':
            state = "|0⟩"
        elif bit == 1 and basis == '+':
            state = "|1⟩"
        elif bit == 0 and basis == 'x':
            state = "|+⟩"
        else:
            state = "|-⟩"
        
        return qc, state
    
    def prepare_all_qubits(self):
        """Encode all bits into quantum circuits"""
        self.circuits = []
        self.states = []
        
        for bit, basis in zip(self.bits, self.bases):
            circuit, state = self.encode_bit(bit, basis)
            self.circuits.append(circuit)
            self.states.append(state)
        
        return self.circuits
    
    def get_data(self):
        """Return all Alice's data"""
        return {
            'bits': self.bits,
            'bases': self.bases,
            'states': self.states
        }