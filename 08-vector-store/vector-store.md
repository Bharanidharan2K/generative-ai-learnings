# Vector Store

## What is a Vector Store?

A **vector store** is a database designed to store **vectors (numerical
representations of data)** and retrieve them based on **similarity**
instead of exact keyword matching.

In simple terms:

-   A **vector** is just a **list of numbers (1-D array)**.
-   These numbers represent the **meaning or context of a word or
    sentence**.
-   Words with **similar meaning will have vectors that are close to
    each other**.

Example:

    King  → [0.12, 0.87, 0.44]
    Queen → [0.11, 0.85, 0.46]
    Car   → [0.91, 0.10, 0.33]

Here:

-   **King and Queen** vectors are close together.
-   **Car** is far away.

So the vector represents the **semantic meaning** of the word.

------------------------------------------------------------------------

## Why Do We Need a Vector Store?

Traditional databases work like this:

``` sql
SELECT * FROM documents WHERE text = "car"
```

This means they only return **exact keyword matches**.

But in AI applications we want something smarter.

Example:

User query:

    vehicle insurance

But the document contains:

    car insurance

A normal database may **not match this**.

A **vector store solves this problem** by storing the **meaning of the
text**, not just the text itself.

So it can understand that:

    car ≈ vehicle
    doctor ≈ physician
    purchase ≈ buy

This is why **vector databases are used in AI applications like RAG
(Retrieval Augmented Generation)**.

------------------------------------------------------------------------

## How Does a Vector Store Work?

### Step 1 --- Convert text to embeddings

Text is converted into **vectors (embeddings)** using an **embedding
model**.

Example:

    "Artificial Intelligence is powerful"

becomes

    [0.23, 0.45, 0.67, 0.12, ...]

------------------------------------------------------------------------

### Step 2 --- Store vectors in a vector database

These vectors are stored along with metadata like:

-   id
-   document
-   metadata
-   embeddings

------------------------------------------------------------------------

### Step 3 --- Query using similarity search

When a user asks a question:

    "What is AI?"

The query is also converted into a vector.

Then the system finds **the closest vectors** in the database using
**distance calculations**.

Common similarity methods:

-   Cosine similarity
-   Euclidean distance
-   Dot product

Vectors that are **closer together represent similar meaning**.

------------------------------------------------------------------------

## Popular Vector Databases

Some well-known vector databases are:

-   ChromaDB
-   Pinecone
-   Weaviate
-   Milvus
-   Qdrant
-   FAISS

In this example we will use **ChromaDB**, which is simple and beginner
friendly.

------------------------------------------------------------------------

# Working with ChromaDB

## Install ChromaDB

``` bash
pip install chromadb
```

------------------------------------------------------------------------

## Step 1 --- Create a Client

A **client** is used to connect to the vector database.

### In-Memory Client

-   Data exists **only during runtime**
-   Data will be **lost when the program stops**

``` python
import chromadb

client = chromadb.Client()
```

### Persistent Client

-   Data is stored **on disk**
-   Data remains even after restarting the program

``` python
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
```

------------------------------------------------------------------------

## Step 2 --- Create a Collection

A **collection** in ChromaDB is similar to a **table in a database**.

A collection can store:

-   ids
-   embeddings
-   documents
-   metadata

``` python
collection = client.create_collection(name="collection1")
```

------------------------------------------------------------------------

## Step 3 --- Add Data to the Collection

``` python
collection.add(
    ids=["1", "2", "3"],
    embeddings=[
        [0.1, 0.2, 0.3],
        [0.2, 0.3, 0.4],
        [0.3, 0.4, 0.5]
    ],
    metadatas=[
        {"name": "Benny"},
        {"name": "Abi"},
        {"name": "Kowsalya"}
    ]
)
```

------------------------------------------------------------------------

## Step 4 --- Retrieve Stored Data

``` python
collection.get(
    ids=["1", "2", "3"],
    include=["embeddings", "metadatas"]
)
```

------------------------------------------------------------------------

## Step 5 --- Add Documents

``` python
collection.add(
    ids=["4"],
    embeddings=[[0.4, 0.5, 0.6]],
    documents=[
        "Bharani is working as a software engineer at Valorem"
    ]
)
```

------------------------------------------------------------------------

## Step 6 --- Retrieve Everything

``` python
collection.get(
    ids=["1", "2", "3", "4"],
    include=["embeddings", "metadatas", "documents"]
)
```

------------------------------------------------------------------------

# Important Concept: Similarity Search

The main purpose of vector databases is **similarity search**.

Instead of searching by keyword, we search by **vector closeness**.

Example:

Query:

    software engineer

Closest result:

    Bharani is working as a software engineer at Valorem

Even if the exact sentence is not typed by the user.

------------------------------------------------------------------------

# Where Vector Stores Are Used

## RAG Applications

Example:

    ChatGPT + Company Documents

The vector database retrieves the **relevant documents** before
generating answers.

------------------------------------------------------------------------

## Semantic Search

Example:

Query:

    How to fix my laptop?

Result:

    Troubleshooting computer issues

------------------------------------------------------------------------

## Recommendation Systems

Examples:

-   Netflix recommendations
-   Amazon product suggestions

------------------------------------------------------------------------

# Summary

A **vector store** is a database that stores **embeddings (vectors)**
and retrieves information based on **similarity instead of exact keyword
matching**.

Key ideas:

-   Text → converted to **vectors**
-   Similar meanings → **vectors are closer**
-   Vector DB → finds **nearest vectors**
-   Used heavily in **AI and RAG systems**
