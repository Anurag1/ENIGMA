from enigma_core.cognitive_core import Enigma

def main():
    print("\n" + "="*60)
    print("      Project Enigma: A Sovereign, Self-Improving Quantum AGI")
    print("="*60)
    print("Enigma is online. Give it a high-level goal that may require quantum computation.")
    print("\nExample Goals:")
    print("  - 'Find the prime factors of 15'")
    print("  - 'What are the prime factors of 35?'")
    print("\nType 'exit' to quit.")
    print("-"*60)

    enigma_agi = Enigma()

    while True:
        try:
            prompt = input("\n[User Goal]> ")
            if prompt.lower() == 'exit':
                print("Enigma signing off.")
                break
            
            response = enigma_agi.process(prompt)
            print(f"\n[Enigma]> Task completed.\n--- FINAL OUTPUT ---\n{response}")
        except Exception as e:
            print(f"A critical error occurred in the cognitive core: {e}")

if __name__ == "__main__":
    main()