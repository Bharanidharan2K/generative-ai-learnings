# 🚀 LangGraph Session - Complete Guide

> **LangGraph** is a famous framework to build AI applications with complex workflows.

---

## 🤔 Why LangGraph/LangChain?

Before learning any technology, we need to understand the **WHY**, **WHAT**, and **HOW** parts, right?

### Problems Without Using LangGraph/LangChain

#### 1️⃣ Vendor Lock-in

Switching AI models usually requires:
- **Rewriting API calls** - Different syntax for OpenAI, Anthropic, Google, etc.
- **Adjusting authentication** - Each provider has different auth methods
- **Changing input/output formats** - Response structures vary across providers

**Example:** If you built your app with OpenAI and want to switch to Claude, you'd need to rewrite everything!

#### 2️⃣ Using Multiple LLMs for Different Tasks

Different tasks require different models for optimal results:
- **Summarization** - Use one model
- **Translation** - Use another specialized model  
- **Reasoning** - Use a different powerful model

These frameworks help with **ease of configuration** even for multi-LLM setups!

---

## 🎯 What is LangGraph/LangChain?

The names themselves tell us what they do!

### LangChain

**Lang** → Language Model  
**Chain** → Chaining things together

#### What does "Chaining" mean?

Chaining tasks means linking operations in a sequence:
1. **Prompt creation**
2. **Model invocation**  
3. **Response parsing**

All linked using a pipeline operator (`|`)

> 📌 **Note:** LangChain is designed for **sequential problems** - that's why the name says "chain" (chain of tasks/functions)

### LangGraph

**Lang** → Language Model  
**Graph** → Graphical representation

#### What does "Graphical" mean?

Graphical representation contains three key components:

##### 🔵 State
- In software, state is **stored data or information** that a component remembers
- Think of it as the "memory" of your workflow

##### 🔵 Node  
- A **function that performs a specific task**
- Like a worker doing one job

##### 🔵 Edge
- Used for **connecting nodes**
- Defines the flow from one task to another

---

## 🔄 Beyond Sequential: Complex Workflows

LangChain is for **sequential problems**, right?

But what if our workflow needs:

### 1. Parallel Workflow ⚡

**Problem:** Analyzing Customer Product Reviews

You receive a product review and need to analyze it from multiple angles **at the same time**:

```
                    ┌→ Sentiment Analysis (Positive/Negative)
                    │
Customer Review ────┼→ Feature Extraction (What features mentioned?)
                    │
                    └→ Language Detection (English/Spanish/etc.)
```

**Why Parallel?** All three analyses can happen simultaneously - they don't depend on each other!

**Real Example:**
- Review: "This phone has an amazing camera but terrible battery life"
- **Parallel Processing:**
  - Sentiment: Mixed (positive + negative)
  - Features: Camera, Battery
  - Language: English

---

### 2. Hierarchical Workflow 🌲

**Problem:** Writing a Research Report

Like a company with a manager and workers:

```
                    Manager Node
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
   Research Worker  Writing Worker  Formatting Worker
```

**How it works:**
1. **Manager Node** receives task: "Write a report on climate change"
2. **Manager delegates:**
   - Research Worker → Gathers data and facts
   - Writing Worker → Creates content from research
   - Formatting Worker → Formats into professional document
3. **Manager** combines all outputs into final report

**Real Example:**  
Like a team lead assigning different parts of a project to team members, then combining their work!

---

### 3. Conditional Workflow 🔀

**Problem:** Customer Support Chatbot

Different questions need different handling:

```
                    Classify Question
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
   Technical Support   Billing Dept   General Info
```

**How it works:**
1. **Customer asks:** "Why is my bill so high?"
2. **Classification Node:** Detects this is a billing question
3. **Routes to:** Billing Department Node
4. **Response:** Specialized billing agent handles it

**Real Examples:**
- "My app crashed" → Technical Support Node
- "Refund my payment" → Billing Department Node  
- "What are your hours?" → General Info Node

**Why Conditional?** The path taken **depends on the input** - it's not fixed!

---

## 🎓 Summary

| Feature | LangChain | LangGraph |
|---------|-----------|----------|
| **Best For** | Sequential tasks | Complex workflows |
| **Structure** | Linear pipeline | Graph with nodes & edges |
| **Flexibility** | Limited to chains | Parallel, Hierarchical, Conditional |
| **Use Case** | Simple workflows | AI agents, multi-step reasoning |

---

## 💡 Key Takeaways

✅ **LangChain** = Sequential processing (A → B → C)  
✅ **LangGraph** = Complex workflows (parallel, hierarchical, conditional)  
✅ Both solve **vendor lock-in** and **multi-LLM** challenges  
✅ Choose based on your **workflow complexity**

---

## 💻 Hands-On: Building a Customer Support Bot

Let's build a real **Conditional Workflow** example step by step!

> 🎯 **Goal:** Create a customer support chatbot that categorizes queries, analyzes sentiment, and routes to appropriate handlers.

![LangGraph Flow Diagram](./langgraph-flow.jpg)

📊 **Visual Flow Diagram Above:** See how data flows from Categorize → Analyze Sentiment → Conditional Routing → Final Response!

---

### 📦 Step 0: Setup & Imports

First, let's import everything we need:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model
```

**What we're importing:**
- `TypedDict` - To define our state schema
- `StateGraph` - The main graph builder
- `END` - To mark the end of workflow
- LangChain components - For prompts and LLM calls

---

### 🤖 Step 1: Initialize the LLM

```python
# Using Groq provider with Llama 3.1 8B Instant model
llm = init_chat_model(
    "llama-3.1-8b-instant",
    model_provider="groq",
    temperature=0,  # deterministic outputs
)
```

**Why this matters:** We're using Llama 3.1 8B Instant via Groq with temperature=0 for consistent, deterministic responses.

---

### 🗂️ Step 2: Define State (The Memory)

> **Remember:** State is the "memory" that gets passed between nodes!

```python
class State(TypedDict):
    query: str          # Customer's question
    category: str       # Technical/Billing/General
    sentiment: str      # Positive/Neutral/Negative
    response: str       # Final response to customer
```

**Think of State as:** A shared notebook that all nodes can read from and write to!

---

### ⚙️ Step 3: Create Nodes (The Workers)

> **Remember:** Each node is a function that does ONE specific job!

#### Node 1: Categorize Query

```python
def categorize(state: State) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Categorize the following query into one of these categories ONLY: "
        "Technical, Billing, General.\\n\\n"
        "Query: {query}"
    )
    
    chain = prompt | llm | StrOutputParser()
    
    category = chain.invoke({"query": state["query"]}).strip()
    
    print(f"\\nCategory: {category}")
    
    return {"category": category}  # Updates state["category"]
```

**Job:** Read the query and classify it.

#### Node 2: Analyze Sentiment

```python
def analyze_sentiment(state: State) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Analyze the sentiment of the following query. "
        "Respond ONLY with: Positive, Neutral, or Negative.\\n\\n"
        "Query: {query}"
    )
    
    chain = prompt | llm | StrOutputParser()
    
    sentiment = chain.invoke({"query": state["query"]}).strip()
    
    print(f"Sentiment: {sentiment}")
    
    return {"sentiment": sentiment}  # Updates state["sentiment"]
```

**Job:** Determine if the customer is happy, neutral, or upset.

#### Node 3: Handle Technical Issues

```python
def handle_technical(state: State) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Provide a helpful technical support response for the following query:\\n\\n{query}"
    )
    
    chain = prompt | llm | StrOutputParser()
    
    response = chain.invoke({"query": state["query"]})
    
    return {"response": response}
```

**Job:** Generate technical support response.

#### Node 4: Handle Billing Issues

```python
def handle_billing(state: State) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Provide a helpful billing support response for the following query:\\n\\n{query}"
    )
    
    chain = prompt | llm | StrOutputParser()
    
    response = chain.invoke({"query": state["query"]})
    
    return {"response": response}
```

**Job:** Generate billing support response.

#### Node 5: Handle General Queries

```python
def handle_general(state: State) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Provide a helpful general support response for the following query:\\n\\n{query}"
    )
    
    chain = prompt | llm | StrOutputParser()
    
    response = chain.invoke({"query": state["query"]})
    
    return {"response": response}
```

**Job:** Generate general support response.

#### Node 6: Escalate to Human

```python
def escalate(state: State) -> dict:
    return {
        "response": "Your issue has been escalated to a human support agent due to negative sentiment."
    }
```

**Job:** Handle angry customers by escalating to human agents.

---

### 🔀 Step 4: Create Router (The Traffic Controller)

> **Router decides:** Which node should handle the request next?

```python
def route_query(state: State) -> str:
    # If customer is angry, escalate immediately
    if "negative" in state["sentiment"].lower():
        return "escalate"
    
    # Otherwise, route based on category
    if state["category"].lower() == "technical":
        return "handle_technical"
    elif state["category"].lower() == "billing":
        return "handle_billing"
    else:
        return "handle_general"
```

**Think of this as:** A traffic cop directing cars to the right lane!

---

### 🏗️ Step 5: Build the Graph

> **Now we connect everything together!**

#### 5.1: Initialize StateGraph

```python
workflow = StateGraph(State)
```

**What this does:** Creates an empty graph that will use our `State` schema.

#### 5.2: Add All Nodes

```python
workflow.add_node("categorize", categorize)
workflow.add_node("analyze_sentiment", analyze_sentiment)
workflow.add_node("handle_technical", handle_technical)
workflow.add_node("handle_billing", handle_billing)
workflow.add_node("handle_general", handle_general)
workflow.add_node("escalate", escalate)
```

**What this does:** Registers all our worker functions as nodes in the graph.

#### 5.3: Set Entry Point

```python
workflow.set_entry_point("categorize")
```

**What this does:** Tells the graph: "Start here!"

#### 5.4: Add Regular Edges (Fixed Connections)

```python
# After categorizing, ALWAYS analyze sentiment
workflow.add_edge("categorize", "analyze_sentiment")

# After handling, ALWAYS end
workflow.add_edge("handle_technical", END)
workflow.add_edge("handle_billing", END)
workflow.add_edge("handle_general", END)
workflow.add_edge("escalate", END)
```

**Regular edges:** Fixed connections that always happen.

#### 5.5: Add Conditional Edges (Decision Points)

```python
# After sentiment analysis, USE ROUTER to decide next step
workflow.add_conditional_edges(
    "analyze_sentiment",  # From this node
    route_query            # Use this function to decide
)
```

**Conditional edges:** The path changes based on the router's decision!

---

### 🔨 Step 6: Compile the Graph

```python
app = workflow.compile()
```

**What this does:** 
- Validates the graph structure
- Creates an executable application
- Think of it as: "Building the machine from the blueprint"

---

### 🚀 Step 7: Invoke the App

#### Create a Runner Function

```python
def run_customer_support(query: str):
    # Initialize state with the customer query
    initial_state = {
        "query": query,
        "category": "",
        "sentiment": "",
        "response": ""
    }
    
    # Run the workflow!
    return app.invoke(initial_state)
```

#### Test It!

```python
query = "The price value in my invoice is wrong"

result = run_customer_support(query)

print("\\n\\nComputed Result")
print(f"\\nQuery: {result['query']}")
print(f"\\nCategory: {result['category']}")
print(f"\\nSentiment: {result['sentiment']}")
print(f"\\nResponse: {result['response']}")
```

---

## 📊 Visual Flow Diagram

```
START
  ↓
[Categorize]
  ↓
[Analyze Sentiment]
  ↓
  ├→ If Negative → [Escalate] → END
  ├→ If Technical → [Handle Technical] → END
  ├→ If Billing → [Handle Billing] → END
  └→ If General → [Handle General] → END
```

---

## 🎯 Key Steps Summary

| Step | Action | Purpose |
|------|--------|--------|
| **1** | Define State | Create the shared memory |
| **2** | Create Nodes | Build worker functions |
| **3** | Add Nodes to Graph | Register workers |
| **4** | Set Entry Point | Define starting node |
| **5** | Add Edges | Connect nodes (fixed paths) |
| **6** | Add Conditional Edges | Connect nodes (dynamic paths) |
| **7** | Compile | Build the executable app |
| **8** | Invoke | Run with initial state |

---

## 💡 The LangGraph Recipe

1. 🗂️ **State** → The shared notebook
2. ⚙️ **Nodes** → The workers
3. 🔀 **Edges** → The connections
4. 🔨 **Compile** → Build the machine
5. 🚀 **Invoke** → Run it!

**Try modifying:**
- Add more categories
- Change routing logic
- Add more sentiment levels
- Create your own workflow!

🎉 **Congratulations!** You've built your first LangGraph application!

---

## 📚 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://docs.langchain.com/)
- [Groq API Documentation](https://console.groq.com/docs)
