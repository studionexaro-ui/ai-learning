from fastapi import FastAPI
from llama_cpp import Llama

app = FastAPI()

# Point to the file we downloaded in the Dockerfile
llm = Llama(model_path="ruvltra-claude-code-0.5b-q4_k_m.gguf")

@app.post("/chat")
def chat(prompt: str):
    output = llm(f"Q: {prompt} A: ", max_tokens=150)
    return {"response": output['choices'][0]['text']}