# LangChain

LangChain is an **open-source orchestration framework** designed to simplify the creation of applications using Large Language Models (LLMs). 

LangChain makes the complicated parts of working & building with AI models easier. It helps do this in two ways:

- Integration - Bring external data, such as your files, other applications, and api data, to your LLMs

- Agency - Allow your LLMs to interact with it's environment via decision making. Use LLMs to help decide which action to take next

It acts as the "glue" that connects LLMs to external data sources, APIs, and memory.

* **Core Philosophy:** Move beyond single-prompt interactions to create **autonomous agents** and **data-responsive** workflows.
* **Key Advantage:** It standardizes the interface across different model providers (OpenAI, Anthropic, Google), preventing "provider lock-in."

---

## Core Building Blocks (The Modules)
LangChain categorizes into several essential components:

### A. Model I/O (Input/Output)
* **Prompts:** Reusable instructions. `PromptTemplates` allow you to define a structure (e.g., "Translate {text} to {language}") without hardcoding inputs.
* **Language Models:** A unified interface for both **LLMs** (text-in, text-out) and **Chat Models** (message-in, message-out).
* **Output Parsers:** Converts the LLM's raw string response into structured formats like JSON, CSV, or Pydantic objects.

### B. Retrieval (RAG - Retrieval Augmented Generation)
This allows the LLM to access data it wasn't trained on (e.g., your private PDFs).
* **Document Loaders:** Import data from 100+ sources (PDF, HTML, GitHub).
* **Text Splitters:** Break long documents into smaller "chunks" for the model's context window.
* **Embeddings:** Converting text chunks into numerical vectors.
* **Vector Stores:** Databases (Chroma, FAISS, Pinecone) that store and search these vectors.

### C. Chains (The Workflow)
A "Chain" is a sequence of components. 
* **LCEL (LangChain Expression Language):** The modern way to pipe components together (`Prompt | Model | Parser`).
* **Functionality:** Chains take a user query, process it through a prompt, send it to the LLM, and return the formatted result.

### D. Memory
LLMs are naturally **stateless** (they forget previous questions). Memory components store past interactions.
* **ConversationBufferMemory:** Stores the entire transcript.
* **ConversationSummaryMemory:** Summarizes the chat to save space (tokens).

### E. Agents
Unlike a fixed "Chain," an **Agent** uses the LLM as a reasoning engine to decide *which* action to take and in *what order*.
* **Tools:** Capabilities you give the agent (e.g., Web Search, Calculator, SQL Database access).

---

## How LangChain Works (Execution Flow)

1.  **User Query:** A user asks a question (e.g., "What was the weather in Paris yesterday?").

2.  **Agent Reasoning:** The agent realizes it doesn't know the answer and decides to use a "Search Tool."

3.  **Action:** The tool fetches real-time data from the web.

4.  **Observation:** The tool returns the weather data to the agent.

5.  **Final Response:** The agent synthesizes the data and the original query into a human-friendly answer.

---

## Use Cases
* **Personalized Chatbots:** Using internal company data for customer support.

* **Summarization:** Condensing long legal documents or research papers.

* **Data Analysis:** Using an LLM to write and execute SQL queries based on natural language.

* **Code Assistants:** Building specialized tools for code review or documentation.

---

## Getting Started (Quick Setup)
To begin, you typically need to install the core package and an LLM provider:
```bash
pip install langchain langchain-openai
```
**Environment Configuration:**
```python
import os
os.environ["OPENAI_API_KEY"] = "your_key_here"
```

---

### Summary Table
| Component | Function |
| :--- | :--- |
| **Prompt** | Instructions for the model |
| **Retriever** | Fetches external data |
| **Vector DB** | Stores "meaning" as math (vectors) |
| **Chain** | A fixed sequence of steps |
| **Agent** | A dynamic "thinker" that uses tools |


## LangChain Chains (The LCEL Era)
A "Chain" is a sequence of calls to components. While legacy LangChain had pre-built classes like `LLMChain`, modern development uses **LCEL (LangChain Expression Language)**.

### A. The Anatomy of LCEL
LCEL uses the pipe operator (`|`) to create a declarative chain. It handles streaming, async, and parallel execution automatically.

* **Prompt:** `ChatPromptTemplate` transforms user input into a message list.

* **Model:** The LLM (e.g., GPT-4o, Claude) processes the messages.

* **Output Parser:** Transforms the raw model output into a string, JSON, or Pydantic object.


**Example Code:**
```python
chain = prompt | model | StrOutputParser()
# Execution
result = chain.invoke({"topic": "Quantum Computing"})
```


### B. Advanced Chain Patterns
1.  **RunnableParallel:** Executes multiple chains in parallel. Great for comparing two different LLMs or performing a search and a calculation simultaneously.
    ```python
    from langchain_core.runnables import RunnableParallel

    joke_chain = ChatPromptTemplate.from_template("Joke about {topic}") | llm
    poem_chain = ChatPromptTemplate.from_template("Poem about {topic}") | llm

    # Both chains start at the same time
    map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

    result = map_chain.invoke({"topic": "coffee"})
    ```

2.  **RunnablePassthrough:** Passes data through a step unchanged (useful for maintaining the original user query for later steps).
    ```python
    from langchain_core.runnables import RunnablePassthrough

    def fake_retriever(query):
        return "The sky is blue because of Rayleigh scattering."

    setup_and_retrieval = RunnableParallel (
        context=fake_retriever, 
        question=RunnablePassthrough()
    )

    prompt = ChatPromptTemplate.from_template("Context: {context} \nQuestion: {question}")
    rag_chain = setup_and_retrieval | prompt | llm

    print(rag_chain.invoke("Why is the sky blue?"))
    ```

3.  **RunnableLambda:** Allows you to inject custom Python functions into the chain.
    ```python
    from langchain_core.runnables import RunnableLambda

    def count_words(text: str) -> int:
        return len(text.split())

    word_counter = RunnableLambda(count_words)
    chain = prompt | llm | StrOutputParser() | word_counter

    count = chain.invoke({"topic": "space"})
    print(f"The LLM's response was {count} words long.")
    ```

4. **RunnableBranch** (Dynamic Routing / Configuration)
This allows the chain to choose a path based on the input.

    Use Case: Routing a query to a "Math Agent" if it contains numbers, or a "Creative Agent" if it asks for a story.

    ```python
    from langchain_core.runnables import RunnableBranch

    # Define different paths
    math_chain = ChatPromptTemplate.from_template("Solve this math: {input}") | llm
    general_chain = ChatPromptTemplate.from_template("Answer this: {input}") | llm

    # Route based on a condition
    branch = RunnableBranch(
        (lambda x: "calculate" in x["input"].lower(), math_chain),
        general_chain
    )

    full_chain = {"input": RunnablePassthrough()} | branch
    print(full_chain.invoke({"input": "Please calculate 2+2"}))
    ```

---

## LangChain Memory (State Management)
Memory is what allows an LLM to "remember" previous parts of a conversation. Because LLMs are **stateless**, you must manually pass the history back to the model with every new request.

### A. Memory Types
| Type | Use Case | Pros/Cons |
| :--- | :--- | :--- |
| **ConversationBuffer** | Simple Chatbots | **Pros:** Accurate. **Cons:** Tokens grow fast. |
| **Window Buffer** | Short-term Memory | **Pros:** Keeps only the last $K$ interactions. |
| **Summary Memory** | Long Conversations | **Pros:** Uses an LLM to summarize old history. Saves tokens. |
| **Entity Memory** | Complex Context | **Pros:** Remembers specific facts about entities (e.g., "User's dog is named Max"). |

### B. The Modern Standard: `ChatMessageHistory`
In production, we no longer store memory in-memory (RAM). We use external databases:
* **Postgres/Redis:** Best for high-speed web apps.
* **MongoDB:** Great for flexible document storage.

---

### Langchain LCEL memory component

#### 1. The Core Components
To add memory to an LCEL chain, you need:
1.  **A Store:** Where the messages live (e.g., `ChatMessageHistory`).
2.  **A Prompt:** That includes a placeholder for `history`.
3.  **A Wrapper:** The `RunnableWithMessageHistory` class, which handles the "loading" and "saving" logic automatically.

---

#### 2. Basic Implementation
In this setup, we define the logic and then wrap it so it knows how to distinguish between different users or sessions.

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# 1. Define the LLM and Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"), # Where history will be injected
    ("human", "{question}")
])

model = ChatOpenAI(model="gpt-4o")

# 2. Create the Chain
chain = prompt | model

# 3. Manage State (The Store)
# In a real app, this would be a database (Redis, Postgres, etc.)
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# 4. The "Magic" Wrapper
with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)
```

#### 3. Running the Chain with Sessions
When you invoke the chain, you must provide a `session_id`. This allows the AI to remember "User A" while having a fresh conversation with "User B."

```python
config = {"configurable": {"session_id": "user_123"}}

# First interaction
response1 = with_message_history.invoke(
    {"question": "Hi, my name is Gemini."}, 
    config=config
)

# Second interaction (It remembers the name)
response2 = with_message_history.invoke(
    {"question": "What is my name?"}, 
    config=config
)

print(response2.content) # Output: "Your name is Gemini!"
```

#### 4. Key Differences in LCEL Memory
Unlike the old "Chain" objects, LCEL memory follows these rules:

* **Explicit Placement:** You **must** use `MessagesPlaceholder` in your prompt template. The chain won't automatically know where to put the old messages.
* **State Isolation:** Using `session_id` ensures that memory isn't leaked between different users in a web server environment.
* **Post-Processing:** Since the output of an LCEL chain is often a `BaseMessage` object, you might need to add a `StrOutputParser()` at the end of your chain (`chain = prompt | model | StrOutputParser()`) to get clean text back.

#### 5. Persistence (Moving beyond RAM)
The example above uses an in-memory dictionary (`store = {}`), which wipes clean if your script restarts. For production in 2026, you would replace `ChatMessageHistory()` with a persistent backend:

* **Redis:** `RedisChatMessageHistory(session_id, url=...)`
* **Postgres:** `PostgresChatMessageHistory(connection_string, session_id)`
* **MongoDB:** `MongoDBChatMessageHistory(...)`

---

## The Shift: From Memory to "State" (LangGraph)
You must understand that **Memory** is being replaced by **State** in complex agents.

### Why the shift?
Basic Memory is **linear**. But what if an agent needs to:
1.  Search the web.
2.  Analyze the results.
3.  *Go back* and search again if the results were poor?

### How State Works
In **LangGraph**, the "Memory" is a shared schema (a Python Dictionary or Pydantic class) that travels between "Nodes" (steps). 
* **Checkpointers:** LangGraph automatically saves the state of the conversation to a database after every step.
* **Time Travel:** You can "rewind" the state to a previous turn, modify the user's prompt, and re-run the chain from that point.

---

## Practical Implementation: RAG with Memory
When building a Retrieval-Augmented Generation (RAG) system, memory is applied at two stages:
1.  **Query Re-writing:** The system looks at the Chat History + New Question to create a standalone search query.
    * *History:* "I'm traveling to Paris."
    * *New Question:* "What's the weather like there?"
    * *Re-written:* "What is the weather in Paris?"
2.  **Final Answer:** The LLM uses the retrieved context and the history to provide a conversational response.

---

### Common Pitfalls
* **Token Overload:** Blindly passing the entire chat history will eventually crash the model or cost a fortune. Always implement a **Trimming** strategy.
* **Privacy:** Ensure PII (Personally Identifiable Information) is scrubbed from memory before it hits the vector database.
* **Context Fragmentation:** If using Summary Memory, ensure the summary is descriptive enough so the LLM doesn't lose the "nuance" of the original conversation.

---

## Document Loaders with LangChain

* Document loaders in LangChain are used to **convert data from different sources (PDF, CSV, HTML, JSON, etc.) into a standard format called a `Document` object**.

* This standardization helps LLMs **process, analyze, and use external data efficiently**.

---

### Document Object Structure

Each loaded document has:
* **`page_content`** → actual text
* **`metadata`** → extra info (source, type, etc.)
* **`id`** → unique identifier 

This makes all data consistent regardless of origin.

---

### Types of Document Loaders

LangChain supports **200+ loaders**, mainly categorized as:

#### 1. By File Type
* CSV → each row becomes a document
* HTML → full page or split by elements
* Markdown → structured sections
* JSON → parsed via schema
* Word (DOCX) → text extraction
* PDF → multiple parsing strategies 

#### 2. By Data Source
* Websites (URLs)
* Wikipedia
* YouTube
* GitHub
* Local files or cloud sources (AWS, Azure) 

---

### Special Loaders
* **DirectoryLoader** → loads multiple files at once
* **WikipediaLoader** → fetches articles based on queries
* Supports **multithreading & batch processing** for efficiency 

---

### Key Features
* Standardizes data into a **common format**
* Supports **structured + unstructured data**
* Works with **many formats and sources**
* Enables **scalable data ingestion pipelines**

---

### Why It Matters
Document loaders are the **first step in AI pipelines**, especially:
* RAG (Retrieval-Augmented Generation)
* Chatbots with external knowledge
* Semantic search systems
* Document Q&A systems

They **bridge raw data → LLM-ready input**.

---

### Final Insight
> Document loaders don’t store data permanently— they just **load it into memory as structured objects**, which can then be processed, embedded, or stored elsewhere.

*LangChain document loaders convert diverse data sources into standardized `Document` objects so LLMs can use them in workflows like RAG, search, and QA systems.*


## LangGraph

**LangGraph for Stateful Workflows** is a framework designed to build **long-running, stateful, and multi-step AI workflows**—especially useful when you need more control than standard chains or pipelines.

---

### What LangGraph Is?

LangGraph is part of the LangChain ecosystem. It lets you model workflows as a **graph of nodes and edges**, where:
* **Nodes** = functions (LLM calls, tools, logic)
* **Edges** = transitions between steps
* **State** = shared memory passed and updated across steps

Unlike simple chains, LangGraph allows:
* Loops 
* Branching
* Persistent memory
* Human-in-the-loop workflows

---

### Core Concepts

#### 1. State
A central object (usually a dict or TypedDict) that flows through the graph.

Example:
```python
state = {
  "messages": [],
  "user_input": "..."
}
```

Each node:
* Reads from state
* Updates state
* Passes it forward

#### 2. Nodes
Functions that operate on the state.
```python
def chatbot_node(state):
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}
```

#### 3. Edges (Control Flow)
Edges define **what runs next**:
* Linear flow
* Conditional branching
* Loops

```python
graph.add_edge("chatbot", "tool_executor")
```

#### 4. Conditional Routing
Dynamic decision-making:
```python
def route(state):
    if "search" in state["messages"][-1]:
        return "search_node"
    return "chatbot"

graph.add_conditional_edges("chatbot", route)
```

#### 5. Cycles (Loops)
Unlike traditional DAGs, LangGraph supports loops:
```python
graph.add_edge("tool_executor", "chatbot")
```

This enables:
* Agent-like behavior
* Iterative reasoning
* Tool retry loops

---

### Example: Simple Stateful Chat Agent
```python
from langgraph.graph import StateGraph

graph = StateGraph(dict)

graph.add_node("chatbot", chatbot_node)
graph.add_node("tools", tool_node)

graph.set_entry_point("chatbot")

graph.add_conditional_edges(
    "chatbot",
    route,
)

graph.add_edge("tools", "chatbot")

app = graph.compile()
```

---

### Why Use LangGraph?

#### 1. True Stateful Workflows
Unlike stateless APIs, LangGraph:
* Maintains conversation history
* Tracks intermediate outputs
* Supports memory across steps

#### 2. Looping & Agents
Perfect for building:
* AI agents
* Tool-using systems
* Self-correcting pipelines

#### 3. Branching Logic
You can:
* Route based on LLM output
* Create decision trees
* Implement fallback strategies

#### 4. Human-in-the-Loop
Pause and resume workflows:
* Approval steps
* Manual corrections
* Async workflows

---

### LangGraph vs Traditional Chains

| Feature       | Chains  | LangGraph |
| ------------- | ------- | --------- |
| Linear flow   | ✅       | ✅         |
| Branching     | ❌       | ✅         |
| Loops         | ❌       | ✅         |
| Memory        | Limited | Strong    |
| Agent control | Limited | Full      |


---

### Common Use Cases
* AI agents with tools (search, DB, APIs)
* Document processing pipelines
* Multi-step reasoning systems
* Stateful chatbots
* Retry / error-handling workflows
* Approval-based flows (human review)

---

### Mental Model
Think of LangGraph like:
* **Finite State Machine + LLM intelligence**
* Or **Airflow for AI agents**
* Or **Backend logic for autonomous systems**

---

### When You Should Use It
Use LangGraph if:
* Your workflow is **not strictly linear**
* You need **memory + iteration**
* You want **fine-grained control over agent behavior**

Avoid it if:
* You just need a simple prompt → response pipeline

---
