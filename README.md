---
title: Smart GPT with Tools
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.32.0"
app_file: frontend.py
pinned: false
---


# 🤖 Smart GPT with Tools – Intelligent LangGraph Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python"/>
  <img src="https://img.shields.io/badge/LangGraph-latest-green.svg" alt="LangGraph"/>
  <img src="https://img.shields.io/badge/LangChain-latest-yellow.svg" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Groq-LLM-orange.svg" alt="Groq"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-red.svg" alt="Streamlit"/>
</p>

<p align="center">
  <strong>An intelligent chatbot built with LangGraph that uses conditional tool routing, reflection-based validation, and multi-tool reasoning for high-quality responses.</strong>
</p>

<p align="center">
  <a href="#-features">✨ Features</a> •
  <a href="#-architecture">🏗️ Architecture</a> •
  <a href="#-project-structure">📁 Project Structure</a> •
  <a href="#-quick-start">🚀 Quick Start</a> •
  <a href="#-how-it-works">🔬 How It Works</a>
</p>

---

## �🎯 Overview

Smart GPT with Tools is a **LangGraph-powered conversational AI system** that intelligently decides:

- when to answer directly,
- when to use external tools,
- and when to reflect and improve its own responses.

Unlike linear chat pipelines, this system uses **graph-based control flow** to route queries through tools, validation, and refinement stages before delivering the final answer.

The result is a chatbot that is **faster, more accurate, and more reliable**.

---

## 💡 Why This Project

Traditional chatbots:
- Call tools unnecessarily
- Return unverified answers
- Lack self-correction

This project demonstrates how to build:
- conditional reasoning flows,
- reflection-based quality assurance,
- and tool-augmented intelligence

It closely resembles **production-grade agent systems** used in real-world GenAI applications.

---

## ✨ Features

### 🎯 Intelligent Routing
- Conditional tool execution using LangGraph
- Direct LLM responses for simple questions
- Automatic decision-making by the model

### 🔧 Multi-Tool Capabilities
- DuckDuckGo web search for real-time information
- Calculator for mathematical expressions
- Easily extensible tool interface

### 🔍 Quality Assurance
- Reflection node validates every response
- Improves clarity, correctness, and completeness
- Prevents low-quality or partial answers

### 💬 Advanced Chat Experience
- Conversation history with memory
- Multi-threaded chat sessions
- Persistent state using checkpointer
- Streaming token-by-token responses

---

## 🏗️ Architecture

### High-Level Flow

```

User Query
│
▼
Chat Node
│
▼
Conditional Router
│
├──► Tool Execution (Search / Calculator)
│           │
│           ▼
│       Chat Node
│
└──► Reflection Node
│
▼
Final Response

```

### Why LangGraph

LangGraph enables:
- conditional edges
- tool-aware routing
- validation loops
- clean separation of responsibilities

---

## 🔬 How It Works

### 1. Chat Node
Receives user input and invokes the LLM with tool bindings.

### 2. Conditional Router
Inspects the LLM output:
- tool call detected → route to tool execution
- no tool needed → route directly to reflection

### 3. Tool Execution
Executes requested tools such as:
- web search
- calculator

### 4. Reflection Node
Evaluates the response for:
- correctness
- clarity
- completeness

Improves the answer if needed before returning it.

### 5. Memory Management
- Thread-based conversation separation
- Full chat history retained per session
- Supports multi-user and multi-chat workflows

---

## 🛠️ Tech Stack

| Component        | Technology            |
|------------------|-----------------------|
| Orchestration    | LangGraph             |
| LLM Framework    | LangChain             |
| LLM Provider     | Groq                  |
| Web Search       | DuckDuckGo            |
| UI               | Streamlit             |
| Language         | Python                |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API key

### Environment Setup

Create a `.env` file:

```

GROQ_API_KEY=your_groq_api_key

````

### Install Dependencies

```bash
pip install -r requirements.txt
````

### Run the App

```bash
streamlit run frontend.py
```

The app will open at `http://localhost:8501`.

---

## 📁 Project Structure

```
Smart_Gpt_with_tools/
├── src/
│   ├── states/
│   │   └── state.py              # ChatState definition
│   ├── llms/
│   │   └── llm.py                # LLM + tool setup
│   ├── nodes/
│   │   └── node.py               # Chat, router, reflection nodes
│   └── graphs/
│       └── graph_builder.py      # LangGraph construction
├── backend.py                    # Chatbot initialization
├── frontend.py                   # Streamlit UI
├── requirements.txt              # Dependencies
├── pyproject.toml                # Project config
└── README.md
```

---

## 🧪 Example Queries

Direct response:

* What is Python?
* Explain machine learning

Tool-based:

* What is 456 * 789?
* Latest news about AI
* Current weather in New York

---

## 🔧 Customization

### Change LLM Model

Edit `src/llms/llm.py`:

```python
llm = ChatGroq(model="your-model-name")
```

### Add New Tools

```python
@tool
def custom_tool(input: str) -> str:
    return result
```

### Modify Routing Logic

Edit `route_tools()` in `src/nodes/node.py`.

### Improve Reflection Logic

Customize prompts in `reflect_node()`.

---

## 🚀 Deploy to Hugging Face Spaces

1. Create a new Space → SDK: Streamlit
2. Upload this repository
3. Add `GROQ_API_KEY` in Space Secrets
4. App runs automatically using `frontend.py`

---

## 📊 Why This Project Stands Out

* Not a basic chatbot
* Demonstrates agentic reasoning
* Uses reflection and validation
* Clean, scalable architecture
* Directly aligned with real-world GenAI systems

---

## 🔮 Future Improvements

* Tool result caching
* More specialized tools
* Confidence-based refusal
* Evaluation metrics dashboard
* Multi-agent extensions

---

## 👨‍💻 Author

Vivek Kumar Gupta
AI Engineering Student | GenAI & Agentic Systems Builder

GitHub: [https://github.com/vivek34561](https://github.com/vivek34561)
LinkedIn: [https://linkedin.com/in/vivek-gupta-0400452b6](https://linkedin.com/in/vivek-gupta-0400452b6)
Portfolio: [https://resume-sepia-seven.vercel.app/](https://resume-sepia-seven.vercel.app/)

---

## 📄 License

MIT License © 2025 Vivek Kumar Gupta

