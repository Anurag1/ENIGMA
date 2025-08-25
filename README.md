# Project Enigma: A Sovereign, Self-Improving Quantum AGI

**Project Enigma** is a blueprint for a next-generation AI platform that can intelligently leverage quantum computation. It is not a quantum computer; it is a **sovereign Quantum Operating System** that wraps noisy, complex quantum hardware in an intelligent AGI layer.

This architecture is designed to **mitigate the core limitations of 2025-era quantum computers**, making them robust, accessible, and powerful for real-world problems.

## The Vision: The Quantum Operating System vs. The Quantum Assembly Language

| Limitation of IBM Quantum (2025) | **How Project Enigma Solves It** |
| :--- | :--- |
| **Noise & Decoherence** | A HONet library of `ErrorCorrectionOctaves` learns the specific noise profile of the hardware and applies adaptive error correction. |
| **Complexity & Accessibility** | The **Meta-Mind (LLM)** acts as a "Quantum Compiler," translating high-level user goals (e.g., "factor 15") into the correct quantum algorithm and parameters. No physics PhD required. |
| **Inefficiency & Static Compilation** | A library of `CircuitOptimizerOctaves` learns to compile algorithms into the most efficient possible circuits for the specific hardware's topology. |
| **Limited Scope** | The **Agentic Planner** can solve complex problems that require both classical and quantum steps, orchestrating the entire workflow. |

---

## How to Run the Live Test Demo

This demo simulates Enigma receiving a factoring problem, planning to use Shor's algorithm, and executing it on a classical quantum simulator (Qiskit).

### Step 1: Install Ollama (The Meta-Mind)
1.  Download and install **Ollama** from [https://ollama.com/](https://ollama.com/).
2.  Pull a powerful model to act as the Meta-Mind: `ollama pull llama3`
3.  Ensure the Ollama server is running in the background.

### Step 2: Set Up the Enigma Project
1.  Clone this repository and set up the Python environment:
    ```bash
    git clone https://github.com/your-username/Project-Enigma.git
    cd Project-Enigma
    python -m venv venv && source venv/bin/activate
    ```
2.  Install the dependencies: `pip install -r requirements.txt`

### Step 3: Educate Enigma (Simulated)
Run this script to create the placeholder files for the foundational quantum skills in the HONet library.
```bash
python educate.py