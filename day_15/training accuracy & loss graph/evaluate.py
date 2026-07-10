import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

# Load dataset and reshape/normalize
(_, _), (X_test_raw, y_test) = fashion_mnist.load_data()
X_test = X_test_raw.reshape(-1, 28, 28, 1) / 255.0

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

try:
    model = tf.keras.models.load_model("simple_fashion_mnist_cnn.h5")
    print("Model successfully loaded.\n")
except IOError:
    print("Error: Run 'build_cnn.py' first to generate the model file.")
    exit()

# Evaluate the trained model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Generate Predictions on sample images
predictions = model.predict(X_test[:5])

print("\n--- Sample Predictions Check ---")
for i in range(5):
    predicted_label = np.argmax(predictions[i])
    actual_label = y_test[i]
    print(f"Sample {i+1}:")
    print(f"  Predicted: {class_names[predicted_label]}")
    print(f"  Actual:    {class_names[actual_label]}")