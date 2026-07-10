import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

# 1. Load the Fashion MNIST dataset
print("Loading Fashion MNIST dataset...")
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# Class names mapping for visualization
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

# 2. Visualize 10 sample images with their labels
print("Visualizing 10 sample images...")
plt.figure(figsize=(12, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i], cmap="gray")
    plt.title(class_names[y_train[i]])
    plt.axis("off")
plt.tight_layout()
plt.savefig("sample_predictions.png", bbox_inches="tight", dpi=300)
plt.show()

# 3. Normalize the dataset (Scale pixels from 0-255 to 0-1)
X_train_norm = X_train / 255.0
X_test_norm = X_test / 255.0

print(f"Data Normalized. Training shape: {X_train_norm.shape}")
print(f"Min value: {X_train_norm.min()}, Max value: {X_train_norm.max()}")