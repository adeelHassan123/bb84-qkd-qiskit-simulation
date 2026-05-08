# BB84 Quantum Key Distribution with Qiskit

### Overview
This project implements the BB84 quantum key distribution protocol using IBM's Qiskit framework. It demonstrates how quantum mechanics enables secure key exchange with detectable eavesdropping.

### Setup Instructions

1. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the simulation**
```bash
python main.py
```

### Project Structure
```
bb84-qkd-qiskit/
├── src/           # Source code modules
├── circuits/      # Generated circuit diagrams
├── screenshots/   # Output screenshots
├── report/        # Lab report
└── output/        # Simulation results
```

### Features
- Complete BB84 protocol implementation
- Quantum circuit generation for 8 qubits
- Basis matching analysis
- Eavesdropping detection simulation
- Circuit visualization