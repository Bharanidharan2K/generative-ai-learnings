# Artificial Neural Networks (ANNs)

## Understanding AI, ML, and DL

### What is AI (Artificial Intelligence)?
- Artificially intelligent systems that act, reason, and behave like humans
- The broad field encompassing all intelligent behavior by machines

### What is ML (Machine Learning)?
- A subset of AI
- Enables machines to learn from large datasets to achieve AI capabilities
- Systems improve through experience without being explicitly programmed

### What is DL (Deep Learning)?
- A subset of ML
- Uses neural networks to find loss/error/cost functions
- Identifies how close predicted values are to actual values using mathematical formulas and patterns
- Works with multiple layers (hence "deep")

## Artificial Neural Networks (ANN)

### Concept and Structure
1. **Brain-Inspired Architecture**
   - Inspired by the human brain with interconnected artificial neurons
   - Mimics how biological neurons process information

2. **Network Layers**
   - Connected from input to output through hidden layers
   - Each layer transforms data progressively

3. **Learning Mechanism**
   - Calculates weights and bias to achieve accurate predictions
   - Adjusts parameters through training

### How ANNs Learn Patterns

1. **Feature Extraction**
   - Each hidden layer identifies features and passes them to the next layer
   - Progressive refinement of information

2. **Hierarchical Learning**
   - Each successive layer finds increasingly complex features
   - Simple features → Complex patterns

### Examples of Pattern Recognition

1. **Image Classification**
   - Identifying cats, dogs, humans, or objects
   - Computer vision applications

2. **Regression Tasks**
   - Salary prediction based on years of experience
   - Numerical predictions

## Implementation Workflow

### Steps to Implement Neural Networks

1. **Define the Problem Statement**
   - Clear objective and success metrics

2. **Collect and Prepare Data**
   - Data gathering and preprocessing
   - Cleaning and normalization

3. **Split Data**
   - **Training Data**: Learn patterns from existing data
   - **Test Data**: Validate learned patterns with new data
   - Common split: 80-20 or 70-30

4. **Define the Neural Network Architecture**
   - Number of layers
   - Neurons per layer
   - Activation functions

5. **Train the Neural Network**
   - Forward propagation
   - Backpropagation
   - Parameter updates

6. **Test the Neural Network**
   - Evaluate on unseen data
   - Calculate metrics

7. **Deploy the Neural Network**
   - Production environment
   - API endpoints

8. **Monitor Performance**
   - Track metrics
   - Retrain if needed

## Key Concepts: Parameters

### What are Parameters?
- **Parameters = Weights + Bias**
- Example: LLMs trained on billions of parameters
- More parameters generally mean more capacity to learn

### Weights
1. **Purpose**
   - Measure the importance of connections between nodes
   - Determine how much influence one neuron has on another

2. **Learning Process**
   - Calculated using mathematical patterns
   - Updated during backpropagation

### Bias
1. **Role**
   - A constant value added to the function
   - Allows flexibility in model fitting

2. **Mathematical Importance**
   - Prevents the function from always passing through the origin
   - Enables the model to fit data better

## Mathematical Representation

For a single neuron:

\[ output = activation(\sum (weights \times inputs) + bias) \]

Where:
- **weights**: Learned parameters
- **inputs**: Features from previous layer
- **bias**: Learned offset
- **activation**: Non-linear function

## Next Steps

- [ ] Implement a simple ANN from scratch
- [ ] Explore different activation functions
- [ ] Study backpropagation in detail
- [ ] Build a project: Handwritten digit recognition

## Resources

- Neural Networks and Deep Learning by Michael Nielsen
- Deep Learning Specialization - Andrew Ng
- PyTorch/TensorFlow official tutorials

---

*Notes compiled from: February 2026*