class Prompt:

    def create_prompt(self, query, retrieved_results):

        context = ""

        for i, result in enumerate(retrieved_results):
            context += f"Context {i + 1}:\n"
            context += result["chunk"]
            context += "\n\n"

        prompt = f"""
You are an AI assistant for NovaTech Solutions.

Answer the user's question using ONLY the information provided in the context.

If the answer cannot be found in the context, say:
"I couldn't find the answer in the provided documents."

Do not use outside knowledge.
Do not make up information.

Context:
{context}

Question:
{query}

Answer:
"""

        return prompt