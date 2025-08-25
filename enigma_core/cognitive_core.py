from .llm_engine import LLMEngine
from .honet_memory import HONetMemory
from .quantum_backend import execute_shor_factorization

class Enigma:
    def __init__(self):
        self.meta_mind = LLMEngine()
        self.memory = HONetMemory()
        self.tools = {
            "shor_factorization": execute_shor_factorization
        }

    def execute_plan(self, plan):
        final_response = ""
        for i, step in enumerate(plan):
            tool_name = step.get("tool")
            param = step.get("parameter")
            print(f"  [Executing Step {i+1}/{len(plan)}: Using tool '{tool_name}' with parameter '{param}']")
            
            # --- This is where the magic happens ---
            # In a real system, it would chain specialists here:
            # 1. Route to AlgorithmOctave (e.g., shor_algorithm)
            # 2. Pass circuit to CircuitOptimizerOctave
            # 3. Pass optimized circuit to ErrorCorrectionOctave
            # 4. Execute on the backend tool.
            
            # For this demo, we directly call the backend tool.
            if tool_name in self.tools:
                # The parameter from the LLM is text, so we convert it to an int.
                try:
                    numeric_param = int(param)
                    result = self.tools[tool_name](numeric_param)
                except ValueError:
                    result = f"Error: The parameter '{param}' is not a valid integer for this tool."
                except Exception as e:
                    result = f"An unexpected error occurred: {e}"
            else:
                result = f"Error: Tool '{tool_name}' not found in my toolset."
            
            final_response += result + "\n"
        return final_response.strip()

    def process(self, prompt):
        print("\n[Enigma Core: Receiving new goal... Devising quantum plan...]")
        known_skills = list(self.memory.skills.keys())
        available_tools = list(self.tools.keys())
        
        plan_json = self.meta_mind.generate_quantum_plan(prompt, known_skills, available_tools)
        
        if not plan_json or "plan" not in plan_json:
            return "[Meta-Mind Error]: I was unable to generate a valid quantum execution plan for your request."

        plan = plan_json["plan"]
        print(f"  [Meta-Mind generated a {len(plan)}-step plan.]")
        
        return self.execute_plan(plan)