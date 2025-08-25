from qiskit_aer.primitives import Sampler as AerSampler
# It's best practice to import from the specific sub-module when possible
from qiskit_algorithms.factorizers.shor import Shor

def execute_shor_factorization(number_to_factor: int) -> str:
    """
    Executes Shor's algorithm on a quantum simulator to factor a number.
    This version is fully compliant with the modern Qiskit 1.0+ library structure.
    """
    print(f"  [Quantum Backend]: Received request to factor {number_to_factor}.")
    if not isinstance(number_to_factor, int) or number_to_factor <= 1 or number_to_factor >= 30:
        return "Error: Input must be an integer between 2 and 29 for this demo."
    if number_to_factor % 2 == 0:
        return f"Classical analysis complete. A factor of {number_to_factor} is 2."

    try:
        sampler = AerSampler()
        shor_instance = Shor(sampler=sampler)
        
        print(f"  [Quantum Backend]: Running Shor's algorithm for N={number_to_factor}. This may take a moment...")
        result = shor_instance.factor(N=number_to_factor)
        
        if result.factors:
            factors = result.factors[0]
            return f"Quantum analysis complete. The prime factors of {number_to_factor} are {factors[0]} and {factors[1]}."
        else:
            return "Quantum analysis did not find factors. Try a different number (like 15 or 21)."

    except Exception as e:
        return f"An error occurred in the quantum backend: {e}"