# Import the necessary libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist.load_data()

# Split the dataset into training and testing sets
(x_train, y_train), (x_test, y_test) = mnist

# Normalize the pixel values to be between 0 and 1 by dividing by 255
x_train, x_test = x_train / 255, x_test / 255

# Build the neural network model
model = models.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

# Train the model
history = model.fit(x_train, y_train, epochs=5)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Make predictions with the model
predictions_for_testdata = model.predict(x_test)

# Plot the first test image and its predicted label
plt.imshow(x_test[0], cmap='gray')
plt.title(f'Predicted label: {np.argmax(predictions_for_testdata[0])}')
plt.show()

# Plot training loss over epochs
plt.plot(history.history['loss'])
plt.title('How much training is enough - Training Loss vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Training Loss')
plt.show()