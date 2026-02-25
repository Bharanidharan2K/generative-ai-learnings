# Recurrent Neural Networks (RNN) – Intuition Notes

Recurrent Neural Networks (RNNs) are a type of neural network designed to handle **sequential data** – data where the **order matters**, like sentences, time-series, or speech. Unlike feedforward networks such as ANN and CNN, RNNs can **remember previous information** and use it when processing new inputs.

---

## Why Do We Need RNNs?

Many real-world problems involve sequences:

- Sentences in a paragraph
- Stock prices over time
- Audio signals or sensor readings

In these cases, the **meaning or value at the current step depends on what came before it**. RNNs are built to handle this.

### 1. Handling Sequential Data

RNNs process inputs **one step at a time**, while carrying a **hidden state** (memory) from previous steps.

- At each step, the RNN sees:
  - The current input (e.g., current word or current time-step value)
  - The previous hidden state (what it remembers so far)
- It updates its hidden state and optionally produces an output.

This makes RNNs ideal for:
- Language modeling and next-word prediction
- Speech recognition
- Time-series forecasting (stocks, weather, sensors)

### 2. Capturing Temporal Dependencies

Unlike CNNs or simple feedforward networks, RNNs have an **internal memory mechanism**:

- They keep track of **past information** through the hidden state.
- This hidden state influences future predictions.
- This is crucial when the meaning depends on context.

**Example 1:**

> "Laptop is used for programming and it also helps for editing."

A feedforward network that looks at only the word "it" in isolation cannot easily know what "it" refers to.  
An RNN, by reading the sequence word by word, can use its memory (hidden state) to understand that "it" refers to "Laptop".

**Example 2:**

- Stock price prediction: each new value depends heavily on previous days.
- Sentence: "The cat sat on the mat."

Here, the word "cat" influences the correct interpretation of later words like "sat" and "mat". RNNs can carry that earlier information forward.

---

## Key Concepts

### Hidden State

The **hidden state** is the core idea behind RNNs.

- It is a vector (a list of numbers) that stores **contextual information** from previous time steps.
- At each time step, the RNN updates this hidden state using:
  - The current input at time $t$ (often written as $x_t$)
  - The previous hidden state $h_{t-1}$
- The new hidden state $h_t$ is like the network's **memory** after seeing data up to time step $t$.

You can think of it as a summary of "everything important seen so far".

### Time Step

A **time step** is one position in the sequence.

- For text: one time step = one word (or character)
- For time-series: one time step = one timestamp (e.g., 1 minute, 1 day)
- For audio: one time step = one frame of audio samples

At each time step:
1. The RNN receives the current input.
2. It updates the hidden state.
3. It may produce an output (like predicting the next word).

---

## Pictorial Representations

### 1. Unrolled RNN Over Time

```text
Sequence: x1, x2, x3, ..., xT

      x1        x2        x3              xT
       |         |         |               |
       v         v         v               v
     +----+    +----+    +----+         +----+
h0 ->|RNN | -> |RNN | -> |RNN |  ... -> |RNN |
     +----+    +----+    +----+         +----+
       |         |         |               |
       v         v         v               v
      y1        y2        y3              yT
```

- $x_t$: input at time step $t$
- $h_t$: hidden state at time step $t$ (memory)
- $y_t$: output at time step $t$
- The arrow from each RNN cell to the next shows the **hidden state being passed forward**.

---

### 2. Single RNN Cell View

```text
          Previous
         hidden state
            h(t-1)
              |
              v
Input x(t) -> [ RNN Cell ] -> h(t)
                   |
                   v
                Output y(t) (optional)
```

Inside the RNN cell, $h_t$ is computed from both $x_t$ and $h_{t-1}$, then passed to the next time step.

---

### 3. Comparing Feedforward vs RNN

```text
Feedforward NN (no memory):

x1, x2, x3 processed independently:
x1 -> NN -> y1
x2 -> NN -> y2
x3 -> NN -> y3

RNN (with memory):

x1, x2, x3 processed in order:

x1, h0 -> RNN -> h1, y1
x2, h1 -> RNN -> h2, y2
x3, h2 -> RNN -> h3, y3
```

- Feedforward: each input is independent; no notion of "sequence".
- RNN: each step **depends on previous steps** through the hidden state.
