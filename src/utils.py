# Helper functions for display and analysis
from src.alice import Alice
from src.bob import Bob 

def print_header(title):
    """Print formatted header"""
    print("\n" + "="*80)
    print(f" {title}")
    print("="*80)

def print_subheader(title):
    """Print subheader"""
    print(f"\n--- {title} ---")

def print_transmission_table(alice, bob):
    """Print complete transmission results"""
    print_header("QUANTUM TRANSMISSION LOG")
    
    print(f"{'#':<4} {'Alice Bit':<10} {'A-Basis':<8} {'State':<10} {'B-Basis':<8} {'Result':<8} {'Match':<6} {'Correct':<8}")
    print("-"*80)
    
    matches = 0
    correct = 0
    
    for i in range(len(alice.bits)):
        basis_match = (alice.bases[i] == bob.bases[i])
        if basis_match:
            matches += 1
        
        bit_correct = (alice.bits[i] == bob.results[i])
        if bit_correct:
            correct += 1
        
        match_sym = "✓" if basis_match else "✗"
        correct_sym = "✓" if bit_correct else "✗"
        
        print(f"{i:<4} {alice.bits[i]:<10} {alice.bases[i]:<8} {alice.states[i]:<10} {bob.bases[i]:<8} {bob.results[i]:<8} {match_sym:<6} {correct_sym:<8}")
    
    print("-"*80)
    return matches, correct

def calculate_accuracy(alice_bits, bob_results):
    """Calculate accuracy percentage"""
    total = len(alice_bits)
    correct = sum(1 for a, b in zip(alice_bits, bob_results) if a == b)
    return (correct / total) * 100, correct, total

def analyze_basis_matching(alice_bases, bob_bases, alice_bits, bob_results):
    """Analyze accuracy by basis matching vs mismatching"""
    match_correct = 0
    match_total = 0
    mismatch_correct = 0
    mismatch_total = 0
    
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            match_total += 1
            if alice_bits[i] == bob_results[i]:
                match_correct += 1
        else:
            mismatch_total += 1
            if alice_bits[i] == bob_results[i]:
                mismatch_correct += 1
    
    return {
        'match': {'correct': match_correct, 'total': match_total, 'pct': (match_correct/match_total*100) if match_total > 0 else 0},
        'mismatch': {'correct': mismatch_correct, 'total': mismatch_total, 'pct': (mismatch_correct/mismatch_total*100) if mismatch_total > 0 else 0}
    }

def print_analysis(alice_bits, bob_results, matches, total):
    """Print complete analysis"""
    accuracy, correct, total = calculate_accuracy(alice_bits, bob_results)
    analysis = analyze_basis_matching(alice.bases, bob.bases, alice_bits, bob_results)
    
    print_header("RESULTS ANALYSIS")
    
    print(f"\n📊 BASIC STATISTICS:")
    print(f"   Total qubits:     {total}")
    print(f"   Correct received: {correct}/{total}")
    print(f"   Overall accuracy: {accuracy:.1f}%")
    
    print(f"\n📐 BASIS ANALYSIS:")
    print(f"   Matching bases:   {analysis['match']['total']} qubits")
    print(f"   → Correct: {analysis['match']['correct']}/{analysis['match']['total']} ({analysis['match']['pct']:.1f}%)")
    print(f"   → Expected: 100%")
    
    print(f"\n   Mismatching bases: {analysis['mismatch']['total']} qubits")
    print(f"   → Correct: {analysis['mismatch']['correct']}/{analysis['mismatch']['total']} ({analysis['mismatch']['pct']:.1f}%)")
    print(f"   → Expected: 50%")
    
    theoretical = (analysis['match']['total'] * 100 + analysis['mismatch']['total'] * 50) / total
    print(f"\n🎯 THEORETICAL EXPECTATION:")
    print(f"   Expected accuracy: {theoretical:.1f}%")
    print(f"   Formula: (matching% × 100%) + (mismatching% × 50%)")
    
    return accuracy

def save_results_to_file(filename, alice, bob, accuracy, analysis):
    """Save results to output file"""
    with open(filename, 'w') as f:
        f.write("BB84 QUANTUM KEY DISTRIBUTION RESULTS\n")
        f.write("="*50 + "\n\n")
        
        f.write("ALICE'S DATA:\n")
        f.write(f"  Bits:  {alice.bits}\n")
        f.write(f"  Bases: {alice.bases}\n")
        f.write(f"  States:{alice.states}\n\n")
        
        f.write("BOB'S DATA:\n")
        f.write(f"  Bases:  {bob.bases}\n")
        f.write(f"  Results:{bob.results}\n\n")
        
        f.write("RESULTS:\n")
        f.write(f"  Overall Accuracy: {accuracy:.1f}%\n")
        f.write(f"  Matching Bases Accuracy: {analysis['match']['pct']:.1f}%\n")
        f.write(f"  Mismatching Bases Accuracy: {analysis['mismatch']['pct']:.1f}%\n")