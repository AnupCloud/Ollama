# Async client
import asyncio
from ollama import AsyncClient

async def chat(prompt: str) -> None:
    """Asynchronously streams responses from the DeepSeek model using Ollama."""
    client = AsyncClient()
    message = {"role": "user", "content": prompt}

    try:
        async for part in await client.chat(model="deepseek-r1:1.5b", messages=[message], stream=True):
            content = part.get("message", {}).get("content", "")
            if content:
                print(content, end="", flush=True)
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    query = "Tell me something about Agent AI for LLM."
    asyncio.run(chat(query))
