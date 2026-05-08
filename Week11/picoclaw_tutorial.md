# PicoClaw

## What is PicoClaw?
* A **hyper-minimal AI agent framework**
* Works as a **CLI-based AI assistant**
* Extremely lightweight (**<10MB RAM**) 
* Runs on:
  * cheap devices (Raspberry Pi, old laptops)
  * modern systems (Mac, Windows)

> “ChatGPT-like assistant running locally on your machine” 

---

## Key Features
* **Ultra-lightweight**
  * No heavy dependencies
  * Fast startup (<1 sec) 

* **Local-first AI**
  * Can use local LLMs (e.g., via Ollama)
  * Keeps data private 

* **Custom AI agents**
  * Behavior defined using simple Markdown
  * No complex coding required 

* **Runs anywhere**
  * Works even on low-cost hardware

---

## Why Use PicoClaw?
* **Privacy** → data stays on your device
* **Cost-effective** → free + low hardware requirements
* **Control** → customize behavior fully
* **Accessibility** → beginner-friendly (no heavy programming needed) 

---

## How PicoClaw Works
* It is a **framework, not the AI model**
* You connect it to:
  * OpenAI / Claude / local models
* It acts as:

  * **interface + agent logic layer**

Flow:
```
User → PicoClaw → AI Model → Response → PicoClaw → Output
```

---

## Installation & Setup (Basic Steps)

### Step 1: Initialize
```bash
picoclaw init
```

* Creates config + project files 

### Step 2: Run
```bash
picoclaw run
```

* Opens chat interface in terminal 

### Step 3: Add AI “Brain”
* Configure API key or local model
* Without this → no intelligent responses

---

## Configuration
* Add:
  * API keys (OpenAI, etc.)
  * Tools (search, integrations)
* Can extend with:
  * web search APIs
  * external services 

---

## What You Can Build
* Personal AI assistant
* Automation bots
* Dev tools (log analysis, scripting)
* Smart home controllers
* Research assistants

Key capability:
* Executes tasks
* Maintains context
* Integrates with tools

---

## Customization
* Agents defined using **Markdown files**
* You can:
  * set personality
  * define rules
  * assign tools

Idea:
> “If you can write text, you can build an AI agent” 

---

## Performance Advantages
* Very low memory usage (<10MB)
* Works on:
  * Raspberry Pi Zero
  * RISC-V boards 
* No heavy Python environments

---

## Limitations
* Not a full AI model itself
* Depends on:
  * external APIs OR local LLMs
* Capability = depends on connected model
* Needs configuration for tools (e.g., search APIs)

---

## Beginner Workflow
1. Install PicoClaw
2. Initialize project
3. Connect AI model
4. Run CLI chat
5. Add tools & customization
6. Build specific use-case

---

## PicoClaw on Windows with Docker Desktop + Ollama

### What is PicoClaw?

PicoClaw is an ultra-lightweight personal AI assistant written in Go. It runs as a single binary with less than 10MB RAM and under 1 second startup time, and supports 16+ chat platforms like Telegram, Discord, and Slack. On Windows, the easiest way to run it is via Docker Desktop.

---

### Prerequisites

Before starting, make sure you have:
- **Docker Desktop** installed and running on Windows
- **Git** installed (to clone the repo)
- **Ollama** running locally with `llama3.1:8b` pulled

---

### Step 1 — Clone the PicoClaw Repository

Open PowerShell or Windows Terminal and run:

```powershell
git clone https://github.com/sipeed/picoclaw.git
cd picoclaw
```

---

### Step 2 — First Run (Generate Config)

The first run auto-generates `docker/data/config.json` and then exits.

```powershell
docker compose -f docker/docker-compose.yml --profile gateway up
```

Wait for the message **"First-run setup complete."** — then the container stops automatically.

---

### Step 3 — Configure Ollama as the LLM Provider

Now edit the generated config file. Open `docker/data/config.json` in any text editor (Notepad, VS Code, etc.).

Ollama is a supported local model server and requires no API key.

Replace or update the `model_list` section like this:

```json
{
  "model_list": [
    {
      "model_name": "llama3.1",
      "model": "ollama/llama3.1:8b",
      "api_base": "http://host.docker.internal:11434"
    }
  ],
  "agents": {
    "defaults": {
      "model_name": "llama3.1"
    }
  }
}
```

> **Key point for Windows:** Docker containers can't reach `localhost` on the host — you must use `host.docker.internal` to reach your Ollama instance. Port `11434` is Ollama's default.

---

### Step 4 — Start PicoClaw (Launcher Mode with Web UI)

The Launcher provides a browser-based setup UI on port **18800**.

```powershell
docker compose -f docker/docker-compose.yml --profile launcher up -d
```

Then open your browser at:
```
http://localhost:18800
```

You'll get a web console to manage models, channels, and the gateway process.

---

### Step 5 — Test with Agent Mode

You can test a quick one-shot question directly:

```powershell
docker compose -f docker/docker-compose.yml run --rm picoclaw-agent -m "Hello, are you working?"
```

Or drop into interactive mode:

```powershell
docker compose -f docker/docker-compose.yml run --rm picoclaw-agent
```

---

### Step 6 — Update PicoClaw Later

To update, pull the latest images and restart:

```powershell
docker compose -f docker/docker-compose.yml pull
docker compose -f docker/docker-compose.yml --profile gateway up -d
```

---

### Troubleshooting Tips

| Problem | Fix |
|---|---|
| Ollama not reachable | Make sure Ollama is running. Use `http://host.docker.internal:11434` not `localhost` |
| `config.json` not generated | Let the first-run container finish completely before editing |
| Web UI not opening | Ensure port 18800 isn't blocked by Windows Firewall |
| Model not found | Run `ollama pull llama3.1:8b` on your host first |

---