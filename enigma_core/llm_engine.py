import ollama
import json

class LLMEngine:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        print(f"LLM Meta-Mind initialized with model: '{self.model_name}'.")

    def get_json_response(self, system_prompt, user_prompt):
        try:
            response = ollama.chat(model=self.model_name, format="json", messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ])
            return json.loads(response['message']['content'])
        except Exception as e:
            print(f"LLM JSON response error: {e}")
            return None

    def generate_quantum_plan(self, prompt, known_skills, available_tools):
        system_prompt = f"""
You are the Quantum Planning Engine for the Enigma AGI. Your task is to take a user's high-level goal and break it down into a sequence of concrete steps.
Each step in the plan must be a JSON object with two keys: "tool" and "parameter".
The "tool" must be one of the available specialist skills or hardware tools: {known_skills + available_tools}.
The "parameter" is the specific input to give to that tool. For a math operation, it's the number.
Your plan should be logical. If the user wants to factor a number, you must use the 'shor_factorization' tool.
Always respond with a single JSON object with a "plan" key.
"""
        return self.get_json_response(system_prompt, prompt)