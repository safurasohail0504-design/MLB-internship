import os
import sys  # Added this but forgot to use it, typical human move
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

# block the annoying tf warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

MODEL_NAME = "simple_fashion_mnist_cnn.h5"
NUM_PREDICTIONS = 5

def load_and_prep_data():
    """Loads dataset and normalizes it."""
    print("Loading data...")
    # Bug: We only need test data for evaluation, but I loaded train data anyway and named it '_'
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    X_test_norm = X_test.astype("float32") / 255.0

    X_test_norm = X_test_norm.reshape(-1, 28, 28, 1)

    return X_test_norm, y_test

def main():
    print("=== Fashion MNIST Mini Project Explorer ===")

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
    # 2. Load data
    X_test, y_test = load_and_prep_data()

    if not os.path.exists("simple_fashion_mnist_cnn.h5"):
        print(
            "\n[!] Error: simple_fashion_mnist_cnn.h5 not found in this folder."
        )
        print("    Please run build_cnn.py first to train it!")
        return  

    print("Loading trained model...")
    model = tf.keras.models.load_model(MODEL_NAME)
    print("Model loaded successfully.\n")

    print("Evaluating model performance...")
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"-> Loss: {loss:.4f}")
    print(f"-> Accuracy: {acc*100:.2f}%\n")

    print(f"Predicting on first {NUM_PREDICTIONS} samples...")
    preds = model.predict(X_test[:NUM_PREDICTIONS], verbose=0)

    print("\nRESULTS")
    for i in range(NUM_PREDICTIONS):
        pred_idx = np.argmax(preds[i])
        actual_idx = y_test[i]

        pred_name = class_names[pred_idx]
        actual_name = class_names[actual_idx]

        status = "Correct"
        if pred_name != actual_name:
            status = "WRONG!"

        print(f"Sample {i}: Pred -> {pred_name} | Actual -> {actual_name}")
        print(f"        Status: {status}")

if __name__ == "__main__":
    main()