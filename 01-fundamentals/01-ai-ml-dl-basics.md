# Fundamentals: AI, ML, and DL

## What is Artificial Intelligence (AI)?

**Artificial Intelligence (AI)** is technology that enables machines to act, reason, and behave like humans. It is the broad field encompassing all intelligent behavior by machines.

### Key Characteristics
- Mimics human cognitive functions
- Performs tasks that typically require human intelligence
- Includes reasoning, learning, problem-solving, and decision-making

### Examples
- Virtual assistants (Siri, Alexa)
- Recommendation systems (Netflix, YouTube)
- Autonomous vehicles
- Game playing (Chess, Go)

---

## What is Machine Learning (ML)?

**Machine Learning (ML)** is a subset of AI that enables machines to learn from data without being explicitly programmed.

### Key Characteristics
- Learns patterns from large datasets
- Improves performance through experience
- Makes predictions or decisions based on data

### How ML Works
1. **Data Collection**: Gather relevant data
2. **Training**: Feed data to algorithm to learn patterns
3. **Validation**: Test on new data
4. **Prediction**: Make decisions on unseen data

### Types of Machine Learning

#### 1. Supervised Learning
- Learns from labeled data (input-output pairs)
- **Examples**: Classification, Regression
- **Use Cases**: Email spam detection, house price prediction

#### 2. Unsupervised Learning
- Learns patterns from unlabeled data
- **Examples**: Clustering, Dimensionality reduction
- **Use Cases**: Grouping similar customers together, identifying unusual patterns in credit card transactions

#### 3. Reinforcement Learning
- Learns through trial and error with rewards/penalties
- **Examples**: Game playing, robotics
- **Use Cases**: Training robots to walk, optimizing traffic light timing

---

## What is Deep Learning (DL)?

**Deep Learning (DL)** is a subset of ML that uses neural networks with multiple layers (hence "deep") to learn complex patterns.

### Key Characteristics
- Uses artificial neural networks
- Automatically extracts features from raw data
- Requires large amounts of data and computational power
- Works with multiple layers for hierarchical learning

### Why "Deep"?
- Multiple hidden layers between input and output
- Each layer learns increasingly complex features
- Example: Image recognition
  - Layer 1: Edges and lines
  - Layer 2: Shapes and textures
  - Layer 3: Object parts
  - Layer 4: Complete objects

---

## The Relationship: AI ⊃ ML ⊃ DL

```
┌─────────────────────────────────────────┐
│ Artificial Intelligence (AI)            │
│  ┌───────────────────────────────────┐  │
│  │ Machine Learning (ML)             │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │ Deep Learning (DL)          │  │  │
│  │  │                             │  │  │
│  │  │ Neural Networks             │  │  │
│  │  │ CNNs, RNNs, Transformers    │  │  │
│  │  └─────────────────────────────┘  │  │
│  │                                   │  │
│  │ Decision Trees, SVM, etc.         │  │
│  └───────────────────────────────────┘  │
│                                         │
│ Rule-based systems, Expert systems      │
└─────────────────────────────────────────┘
```

**Hierarchy:**
- AI is the broadest concept (all intelligent systems)
- ML is a subset of AI (systems that learn from data)
- DL is a subset of ML (neural networks with multiple layers)

---

## Common Applications by Category

### AI Applications
- Chess engines
- Expert systems
- Chatbots
- Voice assistants

### ML Applications
- Email spam filters
- Fraud detection
- Customer churn prediction
- Product recommendations

### DL Applications
- Image recognition
- Natural language processing (ChatGPT, BERT)
- Speech recognition
- Autonomous vehicles
- Medical diagnosis from images

---

## Key Differences Summary

| Feature | AI | ML | DL |
|---------|----|----|-----|
| **Scope** | Broadest | Subset of AI | Subset of ML |
| **Approach** | Rule-based or learning-based | Learning from data | Neural networks |
| **Data Needs** | Varies | Moderate to large | Very large |
| **Human Intervention** | High (rules defined by humans) | Medium (feature engineering) | Low (automatic feature learning) |
| **Examples** | Expert systems, search algorithms | Linear regression, decision trees | CNNs, RNNs, Transformers |

---

## Evolution Timeline

1. **1950s-1980s**: AI - Rule-based systems and expert systems
2. **1990s-2000s**: ML - Statistical learning algorithms gain popularity
3. **2010s-Present**: DL - Neural networks revolutionize AI with breakthroughs in:
   - Computer vision (ImageNet 2012)
   - Natural language processing (Transformers 2017)
   - Generative AI (GPT, DALL-E, Stable Diffusion)

---

## When to Use What?

### Use Traditional ML When:
- You have structured/tabular data
- Dataset is small to medium-sized
- Interpretability is important
- Limited computational resources

### Use Deep Learning When:
- Working with unstructured data (images, text, audio)
- Large dataset available
- High accuracy is critical
- Computational resources are available
- Automatic feature extraction is needed

---

## Next Steps

- [ ] Explore different ML algorithms (Linear Regression, Decision Trees)
- [ ] Understand neural network basics
- [ ] Learn about different deep learning architectures
- [ ] Practice with datasets (MNIST, CIFAR-10)

## Resources

- Andrew Ng's Machine Learning Course (Coursera)
- Deep Learning Specialization by Andrew Ng
- "Hands-On Machine Learning" by Aurélien Géron
- Fast.ai courses

---

*Notes compiled from: February 2026*