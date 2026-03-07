# AI Agents and Model Context Protocol (MCP) Guide

A beginner-friendly guide to understanding AI Agents, Tools, and the Model Context Protocol (MCP).

## Table of Contents

1. [LLM vs Applications](#llm-vs-applications)
2. [What are AI Agents?](#what-are-ai-agents)
3. [Tools Explained](#tools-explained)
4. [Agent Workflow](#agent-workflow)
5. [The Problem: No Standard Tool Protocol](#the-problem-no-standard-tool-protocol)
6. [Solution: Model Context Protocol (MCP)](#solution-model-context-protocol-mcp)
7. [MCP Architecture](#mcp-architecture)

---

## LLM vs Applications

| LLM (Large Language Models) | Applications |
|---|---|
| GPT, Gemini, Deepseek | ChatGPT, Google Gemini, Perplexity |
| Raw AI models that generate text | User-facing apps built on top of LLMs |
| Think "brain" | Think "complete product" |

**Key Difference:** LLMs only generate responses. Applications add UI, tools, and actions.

---

## What are AI Agents?

```
AI Agent = LLM + Tools
```

- **LLM alone:** Can only chat and generate text
- **Agent:** Can take actions using tools

### Example

❌ **LLM:** "Here's how to push code to GitHub..."  
✅ **Agent:** "Pushing your code to GitHub now..."

---

## Tools Explained

**Tools = API Calls + Docstrings**

### Example: GitHub Tool

```python
def push_to_github(repo, branch, code):
    """Pushes code to GitHub repository.
    
    Args:
        repo (str): Repository name
        branch (str): Target branch
        code (str): Code to push
    
    Returns:
        bool: Success status
    """
    # API call to GitHub
    pass
```

**Docstring is key** - Tells LLM what the tool does and how to use it.

---

## Agent Workflow

```
1. User: "Push my code to GitHub"
   ↓
2. App: User query + Tool list (with docstrings)
   ↓
3. LLM: "Call push_to_github('my-repo', 'main', user_code)"
   ↓
4. App: Executes tool → "Code pushed successfully!"
```

### Visual Flow

```
User Query → LLM (with Tools) → Tool Selection → API Call → Action Completed
```

---

## The Problem: No Standard Tool Protocol

```
❌ Zerodha tools: JSON config A
❌ GitHub tools: YAML config B  
❌ Slack tools: Python config C
```

Like APIs without standards:

- REST, GraphQL, gRPC → **Standard protocols exist**
- Tools → **No standard initially**

---

## Solution: Model Context Protocol (MCP)

**MCP = Standardized way to expose tools to any LLM**

> "Provide context to models following a standard protocol"

---

## MCP Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   MCP HOST      │◄──►│ MCP CLIENT   │◄──►│   MCP SERVER    │
│ (IDE/App)       │    │ (1:1 Bridge) │    │ (Tools List)    │
└─────────────────┘    └──────────────┘    └─────────────────┘
```

| Component | Role |
|---|---|
| **MCP Host** | Your application/IDE |
| **MCP Client** | 1:1 communication bridge |
| **MCP Server** | Stores tools with standard config |

---

## Key Takeaways

1. **LLMs** are just the engine; **Applications** build the experience
2. **Agents** extend LLMs with the ability to take actions via **Tools**
3. **Tools** are functions with clear documentation (docstrings)
4. **Agent Workflow** follows a predictable pattern: Query → LLM Decision → Tool Execution → Result
5. **MCP** standardizes how tools are exposed, making them interoperable across different platforms and LLMs
