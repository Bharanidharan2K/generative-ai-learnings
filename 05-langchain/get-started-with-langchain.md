# LangChain

## What is LangChain?

LangChain is a **framework to build AI applications** using Large Language Models (LLMs).

Like any framework, it defines a common way (protocol) to build applications so that you **don't need separate configurations or code for each different LLM provider**. This lets developers focus on **application logic** instead of low-level **API wiring**.

---

## Why LangChain?

1. **Vendor lock-in challenges**  
   Switching AI models usually requires:
   - Rewriting API calls  
   - Adjusting authentication  
   - Changing input/output formats  

   This leads to high migration cost.  
   LangChain acts as a **unified interface** for various LLMs, enabling **seamless model switching** by changing configuration only (like model name or provider), not your entire code.

2. **Use multiple LLMs for different tasks**  
   Different tasks (summarization, translation, reasoning, creative writing) may work best with different models.  
   LangChain provides a **single API** to access multiple LLM providers, making it easier to:
   - Combine models in one workflow  
   - Maintain code  
   - Experiment and optimize per task

---

## Core Features of LangChain

1. **Chat Model**  
   A Chat Model is an **interface to talk with an LLM**.  
   You initialize a chat model once and then use it to send messages and receive responses, regardless of which provider is behind it.

2. **Messages**  
   Messages in LangChain contain two main parts: **role** and **content**.  
   - **Role**: Who is sending the message. Examples: `SystemMessage`, `HumanMessage` (user), `AIMessage` (assistant), `ToolMessage`, etc.  
   - **Content**: The actual text (or data) of the message.  

   This structure helps organize conversations cleanly and is compatible with multiple providers' message formats.

3. **Prompt**  
   A Prompt defines **how we ask the model to do something**.  
   In LangChain, prompts can be turned into **templates** that allow dynamic injection of values (like `{country}`, `{month}`, `{topic}`), making them:
   - Reusable  
   - Structured  
   - Easier to maintain  

   With prompts, you can send input in a **structured way** and often receive output in a more **structured, predictable format**.

---

## Meaning Behind the Name "LangChain"

- **Lang** → stands for **Language Model**.  
- **Chain** → stands for **chaining tasks/functions/actions** together.

For example, you can chain:
- Prompt creation  
- Model invocation  
- Response parsing  

into one pipeline using the pipe operator:

```python
prompt | llm | StrOutputParser()
```

Here:
- `prompt` builds the final text to send to the model  
- `llm` (chat model) generates a response  
- `StrOutputParser()` converts the response into a clean string

This forms a **chain** – a step-by-step flow where the output of one component becomes the input of the next.

---

## Code Examples (Colab-Friendly)

### 1. Install and Setup

```python
!pip install -qU langchain-groq langchain-core

from google.colab import userdata
import os

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
```

### 2. Imports

```python
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

---

### 3. Chat Model Example

```python
model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq"
)

response = model.invoke("What is a neural network?")
print(response.content)
```
This shows how to **talk to an LLM** through a unified chat model interface.

---

### 4. Messages Example (Roles)

```python
messages = [
    SystemMessage(content="You are a helpful assistant to provide an answer only related to cricket. Else say 'I don't know'."),
    HumanMessage(content="Who is Dhoni?")
]

response = model.invoke(messages)
print(response.content)
```
This uses **system + user messages** to control behavior and ask a question.

---

### 5. Prompt Template Example

```python
prompt_template = ChatPromptTemplate.from_template(
    "Suggest me one place to travel in {country} in {month} with a single word"
)

prompt = prompt_template.invoke({"country": "India", "month": "May"})
response = model.invoke(prompt)
print(response.content)
```
This demonstrates **dynamic prompts** with `{country}` and `{month}`.

---

### 6. Simple Chaining

```python
chain = prompt_template | model
response = chain.invoke({"country": "India", "month": "July"})
print(response.content)
```
The chain automatically:
- Fills the template  
- Calls the model  
- Returns the AI message.

---

### 7. Chaining with Output Parser

```python
chain = prompt_template | model | StrOutputParser()
response = chain.invoke({"country": "India", "month": "August"})
print(response)
```
Now you get a **plain string** instead of an `AIMessage` object.

---

### 8. Multi-model Example

```python
model2 = init_chat_model(
    "qwen/qwen3-32b",
    model_provider="groq"
)

movie_prompt = ChatPromptTemplate.from_template(
    "Recommend a popular movie in the {genre} genre."
)

summary_prompt = ChatPromptTemplate.from_template(
    "Write a short 3-line summary of the movie: {movie_name}."
)

chain = (
    movie_prompt
    | model
    | StrOutputParser()
    | {"movie_name": lambda movie: movie}
    | summary_prompt
    | model2
    | StrOutputParser()
)

response = chain.invoke({"genre": "Comedy"})
print(response)
```
This example shows how you can:
- Use **one model** to recommend a movie  
- Use **another model** to summarize it  
all in a single chain.