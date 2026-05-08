# Configuration constants for BB84 protocol

# Number of qubits to send
NUM_QUBITS = 8

# Available bases
BASES = ['+', 'x']

# Basis mapping for display
BASIS_NAMES = {
    '+': 'Plus (Computational)',
    'x': 'X (Hadamard)'
}

# Gate matrices for reference
GATE_X = [[0, 1], [1, 0]]
GATE_H = [[1/1.414, 1/1.414], [1/1.414, -1/1.414]]

# File paths
CIRCUIT_DIR = "circuits"
SCREENSHOT_DIR = "screenshots"
OUTPUT_DIR = "output"
REPORT_DIR = "report"