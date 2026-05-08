# main.py
# Main entry point for BB84 QKD simulation

import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.alice import Alice
from src.bob import Bob
from src.constants import NUM_QUBITS
from src.utils import print_header, print_subheader, print_transmission_table, calculate_accuracy, analyze_basis_matching, save_results_to_file
from src.circuit_demo import generate_complete_circuit_for_lab

def print_analysis(alice, bob, matches, total):
    """Print complete analysis with alice and bob objects"""
    accuracy, correct, total_calc = calculate_accuracy(alice.bits, bob.results)
    analysis = analyze_basis_matching(alice.bases, bob.bases, alice.bits, bob.results)
    
    print_header("RESULTS ANALYSIS")
    
    print(f"\nBASIC STATISTICS:")
    print(f"   Total qubits:     {total}")
    print(f"   Correct received: {correct}/{total}")
    print(f"   Overall accuracy: {accuracy:.1f}%")
    
    print(f"\nBASIS ANALYSIS:")
    print(f"   Matching bases:   {analysis['match']['total']} qubits")
    print(f"   → Correct: {analysis['match']['correct']}/{analysis['match']['total']} ({analysis['match']['pct']:.1f}%)")
    print(f"   → Expected: 100%")
    
    print(f"\nMismatching bases: {analysis['mismatch']['total']} qubits")
    print(f"   → Correct: {analysis['mismatch']['correct']}/{analysis['mismatch']['total']} ({analysis['mismatch']['pct']:.1f}%)")
    print(f"   → Expected: 50%")
    
    theoretical = (analysis['match']['total'] * 100 + analysis['mismatch']['total'] * 50) / total
    print(f"\nTHEORETICAL EXPECTATION:")
    print(f"   Expected accuracy: {theoretical:.1f}%")
    print(f"   Formula: (matching% × 100%) + (mismatching% × 50%)")
    
    return accuracy, analysis

def run_simulation():
    """Run complete BB84 simulation"""
    
    # Create directories
    for dir_name in ['output']:
        os.makedirs(dir_name, exist_ok=True)
    
    print_header("BB84 QUANTUM KEY DISTRIBUTION - COMPLETE LAB")
    print(f"Number of qubits: {NUM_QUBITS}")
    
    # ========== CREATE ALICE AND BOB ==========
    alice = Alice()
    bob = Bob()
    
    # ========== STEP 1: ALICE PREPARES ==========
    print_subheader("STEP 1: Alice generates random bits and bases")
    alice_bits = alice.generate_bits(NUM_QUBITS)
    alice_bases = alice.generate_bases(NUM_QUBITS)
    print(f"   Alice's bits:  {alice.bits}")
    print(f"   Alice's bases: {alice.bases}")
    
    # ========== STEP 2: ENCODE QUBITS ==========
    print_subheader("STEP 2: Alice encodes bits into quantum states")
    alice_circuits = alice.prepare_all_qubits()
    for i, (bit, basis, state) in enumerate(zip(alice.bits, alice.bases, alice.states)):
        print(f"   Qubit {i}: bit={bit}, basis='{basis}' -> {state}")
    
    # ========== STEP 3: BOB CHOOSES BASES ==========
    print_subheader("STEP 3: Bob chooses random measurement bases")
    bob_bases = bob.choose_bases(NUM_QUBITS)
    print(f"   Bob's bases: {bob.bases}")
    
    # ========== STEP 4: BOB MEASURES ==========
    print_subheader("STEP 4: Bob measures received qubits")
    bob_results = bob.measure_all(alice_circuits)
    print(f"   Bob's results: {bob.results}")
    
    # ========== STEP 5: DISPLAY RESULTS ==========
    matches, correct = print_transmission_table(alice, bob)
    
    # ========== STEP 6: ANALYSIS ==========
    accuracy, analysis = print_analysis(alice, bob, matches, NUM_QUBITS)
    
    # ========== STEP 7: SAVE RESULTS ==========
    save_results_to_file("output/results.txt", alice, bob, accuracy, analysis)
    
    # ========== GENERATE CIRCUITS ==========
    print_header("QUANTUM CIRCUIT DIAGRAMS")

    
    print_header("QUANTUM CIRCUIT DIAGRAM - QUANTUM COMPOSER STYLE")

    # Generate a SINGLE complete circuit (like IBM Quantum Composer)
    complete_circuit = generate_complete_circuit_for_lab(alice, bob)


    # ========== PRINT EXPLANATION ==========
    print_header("WRITTEN EXPLANATION - HOW BB84 WORKS")
    
    explanation = f"""
    
    1. ALICE'S PREPARATION:
       • Generates {NUM_QUBITS} random classical bits: {alice.bits}
       • Chooses random bases for each bit: {alice.bases}
       • Encodes each bit using quantum gates
       • Resulting states: {alice.states}
    
    2. QUANTUM TRANSMISSION:
       • Qubits are sent to Bob via quantum channel
       • In real world: photons through fiber optics
    
    3. BOB'S MEASUREMENT:
       • Bob randomly chooses bases: {bob.bases}
       • Measures each qubit in chosen basis
       • Bob's results: {bob.results}
    
    4. RESULTS ANALYSIS:
       • Overall accuracy: {accuracy:.1f}%
       • When bases match: {analysis['match']['pct']:.1f}% correct
       • When bases mismatch: {analysis['mismatch']['pct']:.1f}% correct """
    
    print(explanation)
    
    # ========== FINAL SUMMARY ==========
    print_header("LAB COMPLETION SUMMARY")
    print(f"""
    
    SIMULATION RESULTS:
       • Total qubits: {NUM_QUBITS}
       • Correct bits: {correct}/{NUM_QUBITS}
       • Accuracy: {accuracy:.1f}%
    """)

def main():
    try:
        run_simulation()
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure Qiskit is installed correctly:")
        print("   pip install qiskit qiskit-aer --upgrade")

if __name__ == "__main__":
    main()