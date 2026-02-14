# Neural Network Training: Overfitting, Underfitting, and Normalization

## Table of Contents
- [Training Neural Networks](#training-neural-networks)
- [Overfitting](#overfitting)
- [Underfitting](#underfitting)
- [Normalization](#normalization)
- [Types of Normalization](#types-of-normalization)
- [Why Normalization Matters](#why-normalization-matters)

---

## Training Neural Networks

Training neural networks involves setting hyperparameters through trial and error, which can lead to two common problems:
- **Overfitting**: The model trains too much on training data and fails to generalize to new data
- **Underfitting**: The model receives insufficient data, resulting in poor predictions on both training and testing data

---

## Overfitting

### Definition
Overfitting occurs when a neural network learns the training data too well, including noise and specific patterns that don't generalize to new data.

### Example: Stop Sign Detection
Consider training a model to detect stop signs on highways:
- **Training data**: Red colored boards/lights are stop signs
- **Problem**: The neural network might incorrectly identify a person wearing red clothing standing beside the road as a stop sign, causing the vehicle to stop unnecessarily
- **Root cause**: The model memorized "red color" as the primary feature without understanding the broader context of what constitutes a stop sign

---

## Underfitting

### Definition
Underfitting happens when a neural network doesn't receive enough information during training, resulting in poor performance on both training and testing data.

### Example: Human Classification
Consider training a model to classify humans vs. animals:
- **Training data**: Defined humans as having a nose, two ears, two eyes, and hair
- **Problem**: If a person wears sunglasses (coolers), the model fails to recognize them as human
- **Root cause**: Insufficient training data and oversimplified feature definitions prevent proper generalization

---

## Normalization

### What is Normalization?
Normalization is the process of scaling input data to a specific range, ensuring that all features have similar importance to the neural network.

### Why It's Important: House Price Prediction Example
Consider predicting house prices based on:
- **Number of bedrooms**: Typically ranges from 1-3
- **Square footage**: Ranges from 1,000-10,000 sq.ft

**The Problem**: Without normalization, the neural network assigns higher importance to features with larger numerical values (square footage) while undervaluing smaller-scale features (number of bedrooms), even though both are equally important for accurate predictions.

---

## Types of Normalization

### 1. Min-Max Normalization
Scales data to a fixed range, typically [0, 1] or [-1, 1].

**Formula**:
\[
x_{normalized} = \frac{x - x_{min}}{x_{max} - x_{min}}
\]

**Use case**: When you need data within a specific bounded range.

---

### 2. Z-Score Standardization (Standard Normalization)
Transforms data to have a mean of 0 and standard deviation of 1.

**Formula**:
\[
x_{standardized} = \frac{x - \mu}{\sigma}
\]

Where:
- \(\mu\) = mean of the data
- \(\sigma\) = standard deviation

**Use case**: Works best when dealing with outliers.

**Example with outliers**: Consider the dataset [0, 1, 2, 3, 4, 1000]
- The value 1000 is an outlier because it's significantly larger than other values
- Z-score standardization handles this better than min-max normalization

---

## Why Normalization Matters

### Key Benefits

1. **Avoid Feature Dominance**
   - Ensures no single feature disproportionately influences the model
   - All features contribute fairly to the learning process

2. **Speed Up Convergence**
   - Helps gradient descent reach the optimal minimum faster
   - Reduces training time and computational resources

3. **Improve Accuracy**
   - Makes distance-based models more reliable
   - Enhances overall model performance and prediction quality

---

## Summary

Proper neural network training requires:
- Balancing between overfitting and underfitting through appropriate data and hyperparameter tuning
- Applying normalization techniques to ensure fair feature representation
- Choosing the right normalization method (Min-Max vs. Z-Score) based on your data characteristics

By understanding and implementing these concepts, you can build more robust and accurate neural network models.

---

**Document prepared for**: Generative AI Learning Repository  
**Last Updated**: February 14, 2026