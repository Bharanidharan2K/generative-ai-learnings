# Handwritten Digit Recognition using Neural Networks

A simple deep learning project that classifies handwritten digits from the MNIST dataset using TensorFlow and Keras.

## Overview
This project implements a neural network to recognize handwritten digits (0-9) with 97.59% accuracy on the test dataset.

## Model Architecture
- **Input Layer**: Flattened 28x28 images (784 features)
- **Hidden Layer**: 128 neurons with ReLU activation
- **Output Layer**: 10 neurons with Softmax activation (one for each digit)

## Results
- **Training Accuracy**: ~99.8%
- **Test Accuracy**: 97.59%
- **Loss Function**: Sparse Categorical Crossentropy
- **Optimizer**: Adam

## Requirements
```txt
tensorflow>=2.19.0
numpy>=1.26.0
matplotlib>=3.5.0
