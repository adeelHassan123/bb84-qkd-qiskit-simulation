# src/circuit_demo.py
# Professional Quantum Circuit Visualization - IBM Quantum Composer Style

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import os

def create_complete_bb84_circuit(alice_bits, alice_bases, bob_bases):
    n_qubits = len(alice_bits)
    
    # Create circuit with n_qubits and n_qubits classical bits
    qc = QuantumCircuit(n_qubits, n_qubits)
    
    # Label each qubit for clarity
    for i in range(n_qubits):
        # Add a barrier with label (using comment in circuit)
        pass
    
    # ========== PART 1: ALICE'S ENCODING ==========
    for i, (bit, basis) in enumerate(zip(alice_bits, alice_bases)):
        # Apply gates based on Alice's bit and basis
        if bit == 1:
            qc.x(i)  # X gate for bit 1
        
        if basis == 'x':
            qc.h(i)  # H gate for x-basis
    
    # Barrier to separate Alice's encoding from transmission
    qc.barrier(range(n_qubits))
    
    # ========== PART 2: BOB'S MEASUREMENT ==========
    for i, basis in enumerate(bob_bases):
        if basis == 'x':
            qc.h(i)  # Transform back from x-basis
    
    # Barrier before measurement
    qc.barrier(range(n_qubits))
    
    # ========== PART 3: MEASUREMENT ==========
    for i in range(n_qubits):
        qc.measure(i, i)
    
    return qc

def create_single_qubit_demo():
    qc = QuantumCircuit(4, 4)
    
    # Qubit 0: Bit 0, Basis '+' -> |0>
    # No gates needed
    
    # Qubit 1: Bit 1, Basis '+' -> |1>
    qc.x(1)
    
    # Qubit 2: Bit 0, Basis 'x' -> |+>
    qc.h(2)
    
    # Qubit 3: Bit 1, Basis 'x' -> |->
    qc.x(3)
    qc.h(3)
    
    # Add barriers for visual separation
    qc.barrier()
    
    # Measure all qubits
    for i in range(4):
        qc.measure(i, i)
    
    return qc

def visualize_quantum_composer_style(circuit, title="BB84 Quantum Circuit", filename="quantum_composer_circuit.png", save_dir="circuits"):
    """
    Visualize circuit in IBM Quantum Composer style
    Creates publication-quality circuit diagram
    """
    os.makedirs(save_dir, exist_ok=True)
    
    # Configure matplotlib for quantum composer style
    plt.rcParams['font.family'] = 'monospace'
    plt.rcParams['font.size'] = 12
    plt.rcParams['figure.dpi'] = 150
    
    # Draw circuit with matplotlib (composer style)
    fig = circuit.draw(
        output='mpl',
        style={
            'backgroundcolor': '#FFFFFF',
            'fontsize': 14,
            'subfontsize': 12,
            'displaytext': {
                'x': 'X',
                'h': 'H',
                'measure': 'Meas'
            },
            'cregbundle': False,
            'showindex': True,
            'fold': -1
        },
        scale=1.2,
        plot_barriers=True,
        reverse_bits=False,
        justify='left'
    )
    
    # Improve figure appearance
    ax = fig.gca()
    ax.set_facecolor('#FFFFFF')
    
    # Add title
    fig.suptitle(title, fontsize=16, fontweight='bold', y=0.98)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save high-quality image
    filepath = os.path.join(save_dir, filename)
    fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    
    return filepath

def print_circuit_text(circuit):
    """Print circuit in text format (ASCII art)"""
    print("\n" + "="*80)
    print("QUANTUM CIRCUIT DIAGRAM")
    print("="*80)
    print(circuit.draw(output='text'))
    print("="*80)

def create_professional_bb84_circuit_with_labels(alice_bits, alice_bases, bob_bases):
    """
    Create a professional BB84 circuit with proper labels and sections
    This looks like a real research paper circuit
    """
    n_qubits = len(alice_bits)
    qc = QuantumCircuit(n_qubits, n_qubits)
    
    # Add metadata as comments
    qc.metadata = {
        'protocol': 'BB84',
        'num_qubits': n_qubits,
        'alice_bits': alice_bits,
        'alice_bases': alice_bases,
        'bob_bases': bob_bases
    }
    
    # Create labeled sections using barriers
    for i, (bit, basis, bob_basis) in enumerate(zip(alice_bits, alice_bases, bob_bases)):
        # Alice's encoding section
        if bit == 1:
            qc.x(i)
        if basis == 'x':
            qc.h(i)
    
    # Barrier with label (section separator)
    qc.barrier()
    
    # Bob's measurement preparation section
    for i, bob_basis in enumerate(bob_bases):
        if bob_basis == 'x':
            qc.h(i)
    
    # Barrier before measurement
    qc.barrier()
    
    # Measurement section
    for i in range(n_qubits):
        qc.measure(i, i)
    
    return qc

def save_circuit_components(circuit, save_dir="circuits"):
    """
    Save circuit in multiple formats for different uses
    """
    os.makedirs(save_dir, exist_ok=True)
    
    # 1. Save as matplotlib figure (best quality)
    fig = circuit.draw(output='mpl', style='clifford', scale=1.5)
    fig.savefig(os.path.join(save_dir, 'circuit_matplotlib.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    # 2. Save as text
    with open(os.path.join(save_dir, 'circuit_text.txt'), 'w') as f:
        f.write(str(circuit.draw(output='text')))
    
    # 3. Save as LaTeX (for papers)
    latex_str = circuit.draw(output='latex')
    with open(os.path.join(save_dir, 'circuit_latex.tex'), 'w') as f:
        f.write(latex_str)
    
    return True

def generate_complete_circuit_for_lab(alice, bob):
    """
    Main function to generate the complete circuit for the lab
    This creates a single, beautiful circuit showing everything
    """
    print("\n" + "="*80)
    print("GENERATING PROFESSIONAL QUANTUM CIRCUIT")
    print("="*80)
    
    # Create complete circuit
    circuit = create_complete_bb84_circuit(
        alice.bits, 
        alice.bases, 
        bob.bases
    )
    
    # Print text version for terminal
    print_circuit_text(circuit)
    
    # Save high-quality image
    image_path = visualize_quantum_composer_style(
        circuit,
        title=f"BB84 Protocol - {len(alice.bits)} Qubit Quantum Circuit",
        filename="bb84_quantum_composer_circuit.png"
    )
    
    # Save additional formats
    save_circuit_components(circuit)
    
    print(f"\nCircuit saved to: {image_path}")
    print("Also saved as: circuits/circuit_matplotlib.png")
    print("Text version: circuits/circuit_text.txt")
    print("LaTeX version: circuits/circuit_latex.tex")
    
    return circuit

# Keep original simple functions for compatibility
def create_sample_circuit(bit=1, basis='x'):
    """Simple sample circuit for demonstration"""
    qc = QuantumCircuit(1, 1)
    
    if bit == 1:
        qc.x(0)
    if basis == 'x':
        qc.h(0)
    
    qc.barrier()
    
    if basis == 'x':
        qc.h(0)
    
    qc.measure(0, 0)
    return qc, []

def visualize_circuit(circuit, title, filename=None, save_dir="circuits"):
    """Simple visualization for compatibility"""
    print(f"\n{title}")
    print(circuit.draw(output='text'))
    
    if filename:
        os.makedirs(save_dir, exist_ok=True)
        try:
            fig = circuit.draw(output='mpl', style='clifford')
            filepath = os.path.join(save_dir, filename)
            fig.savefig(filepath, dpi=150, bbox_inches='tight')
            plt.close()
            print(f"Saved: {filepath}")
        except Exception as e:
            print(f"Could not save: {e}")

def generate_all_circuits(alice_circuits, alice_bits, alice_bases, alice_states, save_dir="circuits"):
    """Generate all individual circuits for compatibility"""
    os.makedirs(save_dir, exist_ok=True)
    
    for i, (circuit, bit, basis, state) in enumerate(zip(alice_circuits, alice_bits, alice_bases, alice_states)):
        print(f"\nCircuit {i}: bit={bit}, basis='{basis}', state={state}")
        print(circuit.draw(output='text'))
        
        try:
            fig = circuit.draw(output='mpl', style='clifford')
            fig.savefig(os.path.join(save_dir, f"circuit_{i}.png"), dpi=100, bbox_inches='tight')
            plt.close()
        except:
            pass