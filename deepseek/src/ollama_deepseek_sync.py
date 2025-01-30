# Normal function
import asyncio
import ollama

def ollama_deepseek(prompt: str) -> None:
    # Run a DeepSeek model using Ollama
    response = ollama.chat(
        model="deepseek-r1:1.5b",  # Ensure the model is installed
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)
    # return response['message']['content']

if __name__ == '__main__':
    query = "Tell me something about Agent AI for LLM."
    ollama_deepseek(query)
