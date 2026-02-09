# Hyperparameters, Loss Functions & Training Process

## Neural Network

A computational model inspired by the human brain. Uses interconnected artificial neurons to process information and learn patterns from data.

---

## Hyperparameters

**Hyperparameters** are parameters set before training begins. They control the training process and model performance.

### Key Hyperparameters and Their Importance

1. **Number of Layers**
   - Defines the depth of the network
   - Determines how many layers are needed based on problem complexity

2. **Number of Epochs**
   - Number of times the model sees the entire dataset during training
   - More epochs = more learning opportunities (but risk of overfitting)

3. **Batch Size**
   - Number of training samples processed before updating weights and bias
   - Affects training speed and memory usage

4. **Number of Neurons**
   - How many neurons per layer
   - Based on problem complexity and data dimensionality

5. **Optimizer Function**
   - Determines how to update weights and bias optimally
   - Common choice: **Adam Optimizer**

6. **Activation Function**
   - Introduces non-linearity to the network
   - Enables learning of complex patterns

7. **Learning Rate**
   - Controls the step size for weight updates in each iteration
   - Too high = unstable training, too low = slow convergence

> **Note**: Hyperparameters are set by humans through trial and error. Finding optimal values requires experimentation to avoid overfitting and underfitting.

---

## Loss Functions

**Loss functions** (also called error or cost functions) measure the difference between predicted values and actual values. They quantify how close predictions are to ground truth.

### Types of Loss Functions

#### 1. Mean Squared Error (MSE)
- **Use Case**: Regression problems
- **Purpose**: Calculate error for numerical predictions
- **Formula**: Average of squared differences between predictions and actual values

#### 2. Mean Absolute Error (MAE)
- **Use Case**: Regression problems
- **Purpose**: Alternative to MSE, less sensitive to outliers
- **Formula**: Average of absolute differences

#### 3. Binary Cross Entropy
- **Use Case**: Binary classification problems
- **Purpose**: Two-class output (Yes/No, Valid/Invalid, 0/1)
- **Example**: Spam detection, disease diagnosis

#### 4. Categorical Cross Entropy
- **Use Case**: Multi-class classification with one-hot encoding
- **Purpose**: Multiple classes where labels are encoded as vectors
- **Example**: Image classification with labels [1,0,0], [0,1,0], [0,0,1]

#### 5. Sparse Categorical Cross Entropy
- **Use Case**: Multi-class classification with integer labels
- **Purpose**: Multiple classes where labels are integers
- **Example**: MNIST digit recognition (0-9), where labels are 0, 1, 2... 9

---

## Training Process

### 1. Forward Pass
- Process where input data flows through network layers
- Each layer applies transformations using:
  - Weights
  - Bias
  - Activation functions
- **Goal**: Generate predicted output and calculate how close it is to actual output

### 2. Backward Propagation (Backpropagation)
- Process that adjusts weights and bias based on error from forward pass
- Uses the optimizer function to update parameters
- Works backward through the network layers
- **Goal**: Minimize loss by updating weights and bias

---

## Optimizer Functions

Determines how weights and bias are updated during training.

### Common Optimizers

#### 1. Gradient Descent
- **Characteristics**: Slow, requires entire dataset for each update
- **Use Case**: Simple problems, educational purposes

#### 2. Adam Optimizer
- **Characteristics**: Fast, adaptive learning rates
- **Use Case**: Works well for most real-world problems
- **Why Popular**: Industry standard for deep learning

---

## Activation Functions

Determines whether a neuron should activate and pass information to the next layer. Essential for introducing non-linearity into the network.

### Types of Activation Functions

#### 1. ReLU (Rectified Linear Unit)
- **Use Case**: Hidden layers of deep networks
- **Function**: Returns 0 for negative inputs, keeps positive values unchanged
- **Why Popular**: Simple, fast, effective

#### 2. Softmax
- **Use Case**: Output layer for multi-class classification
- **Function**: Converts raw scores into probabilities that sum to 1
- **Example**: [0.1, 0.7, 0.2] represents 70% confidence for class 2

#### 3. Sigmoid
- **Use Case**: Output layer for binary classification
- **Function**: Outputs values between 0 and 1
- **Interpretation**: Can be treated as probability

---

## Summary Table: Choosing Components

| Problem Type | Loss Function | Output Activation |
|-------------|---------------|-------------------|
| Regression | MSE or MAE | None (Linear) |
| Binary Classification | Binary Cross Entropy | Sigmoid |
| Multi-class (one-hot) | Categorical Cross Entropy | Softmax |
| Multi-class (integer labels) | Sparse Categorical Cross Entropy | Softmax |

**Recommended defaults for training:**
- Optimizer: Adam
- Hidden layer activation: ReLU
- Learning rate: 0.001 (Adam default)
- Batch size: 32 or 64

---

*Notes compiled from: February 2026*