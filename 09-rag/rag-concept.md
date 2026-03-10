# Retrieval-Augmented Generation (RAG)

## What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique where an AI
model first **retrieves relevant information from external data
sources** and then **uses that information to generate an answer**.

Normally, Large Language Models (LLMs) like GPT are trained using a
large amount of **internet data**. However, they **do not know your
private or custom data**, such as:

-   Company documents
-   Internal knowledge bases
-   PDFs
-   Databases
-   Videos

RAG solves this problem by allowing the model to **search your data
first** and then generate answers using that retrieved information.

In simple terms:

    RAG = Retrieve Information + Generate Answer

------------------------------------------------------------------------

# Why Do We Need RAG?

### 1. Models Do Not Know Private Data

LLMs are trained on public data and cannot access your internal
documents.

Example:

    Question: What is our company leave policy?

A normal LLM **cannot answer this correctly** because it does not know
your internal documentation.

With RAG, we can allow the model to access:

-   PDFs
-   Websites
-   Videos
-   Internal documents

The model retrieves the relevant information before answering.

------------------------------------------------------------------------

### 2. Reduces Hallucination

Sometimes LLMs generate answers that **sound correct but are actually
wrong**. This is called **hallucination**.

RAG helps reduce hallucination because the model answers based on
**actual retrieved data**.

------------------------------------------------------------------------

### 3. Allows Up-to-Date Knowledge

LLMs are trained at a specific time and may not know the latest
information.

RAG allows the system to retrieve **new or updated data** from documents
or databases.

------------------------------------------------------------------------

# How RAG Works

Below is the general workflow of a RAG system.

    User Question
          ↓
    Convert Question to Embedding
          ↓
    Search Vector Database
          ↓
    Retrieve Relevant Document Chunks
          ↓
    Send Context + Question to LLM
          ↓
    LLM Generates Final Answer

------------------------------------------------------------------------

# Step 1: Load the Documents

Example: Loading transcript from a YouTube video.

``` python
from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=UabBYexBD4k",
    add_video_info=False,
    language=["en-US"]
)

docs = loader.load()
```

------------------------------------------------------------------------

# Step 2: Split the Documents into Chunks

Large documents are split into **smaller chunks**.

Chunk overlap ensures context is preserved.

``` python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

all_splits = text_splitter.split_documents(docs)
```

------------------------------------------------------------------------

# Step 3: Create Embeddings

Text is converted into **vector embeddings** to represent semantic
meaning.

``` python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)
```

------------------------------------------------------------------------

# Step 4: Store in Vector Database

Embeddings are stored in a **vector database**.

``` python
from langchain_chroma import Chroma

vectorstore = Chroma(
    collection_name="rag",
    embedding_function=embeddings,
    persist_directory="./chroma_genai"
)

vectorstore.add_documents(all_splits)
```

------------------------------------------------------------------------

# Step 5: Create a Retriever Tool

The retriever searches the vector database and returns relevant chunks.

``` python
from langchain.tools import tool

@tool(response_format="content_and_artifact")
def retrieve_context(query: str):

    retrieved_docs = vectorstore.similarity_search(query, k=2)

    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )

    return serialized, retrieved_docs
```

------------------------------------------------------------------------

# Why We Return Two Values

    return serialized, retrieved_docs

  Return Value     Purpose
  ---------------- -------------------------------------------------
  serialized       Context sent to the LLM
  retrieved_docs   Used for debugging, logging, or showing sources

The model only reads the **serialized text**, while the retrieved
documents are used internally.

------------------------------------------------------------------------

# Step 6: Initialize the Model

``` python
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "gpt-4o",
    model_provider="openai"
)
```

------------------------------------------------------------------------

# Step 7: Create an Agent

``` python
from langchain.agents import create_agent

tools = [retrieve_context]

prompt = (
    "You have access to a tool that retrieves context from a Youtube video. "
    "Use the tool to help answer user queries."
)

agent = create_agent(model, tools, system_prompt=prompt)
```

------------------------------------------------------------------------

# Step 8: Ask a Question

``` python
input_message = (
  "What is the context about the document?"
)

for event in agent.stream(
  {"messages": [{"role": "user", "content": input_message}]},
  stream_mode="values"
):
  event["messages"][-1].pretty_print()
```

------------------------------------------------------------------------

# Final RAG Pipeline

    User Question
          ↓
    Embedding
          ↓
    Vector Database Search
          ↓
    Retrieve Relevant Chunks
          ↓
    Send Context + Question to LLM
          ↓
    LLM Generates Final Answer

------------------------------------------------------------------------

# Summary

Retrieval-Augmented Generation (RAG) allows AI systems to:

-   Access external knowledge
-   Work with private documents
-   Reduce hallucinations
-   Generate accurate answers

Common tools used:

-   LangChain
-   OpenAI Embeddings
-   Chroma Vector Database
-   LLMs like GPT
