# Ollama

**What is Ollama?**
- A tool to run large language models locally
- No API key needed

Works with models like:
- Llama 2
- Mistral
- Gemma

> “Docker for LLMs”

## System Requirements
Minimum:
```text
8 GB RAM (16 GB recommended)
CPU works, but GPU is better
macOS / Linux / Windows (WSL)
```

## Using Ollama

### Install ollama
``` curl -fsSL https://ollama.com/install.sh | sh ``` or do it manually from https://docs.ollama.com/

### Install models
Get available model name from https://ollama.com/search 

```bash
ollama run model-name

# example
ollama run llama3.1:8b
```

### Start Ollama
```bash
ollama serve
```

Runs local server at:
```
http://localhost:11434
```

### Remove a model
```ollama rm gemma3```

### List models
```ollama ls```

### Stop a running model
```ollama stop gemma3```

## Python Example:
```python
import requests
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.1:8b",
        "prompt": "Explain transformers simply",
        "stream": False
    }
)
print(response.json()["response"])
```

## Advanced: Custom Models
You can create your own:
```bash
ollama create mymodel -f Modelfile
```

Example Modelfile:
```
FROM mistral
PARAMETER temperature 0.7
SYSTEM "You are a helpful assistant"
```