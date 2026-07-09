# Day 14: Introduction to Deep Learning & Fashion MNIST Classification

What is Deep Learning?

Deep Learning is a subset of Machine Learning inspired by the structure and function of the human brain. It utilizes multi-layered Artificial Neural Networks (ANNs) to automatically learn feature representations from raw data without manual feature engineering.

Machine Learning vs. Deep Learning

* **Machine Learning (ML):** Relies heavily on human intervention for feature extraction (e.g., deciding which columns to use). It performs well on smaller, structured tabular datasets.
* **Deep Learning (DL):** Automatically learns features directly from raw data (like raw pixels in an image). It requires massive amounts of data and computational power (GPUs) to excel, making it ideal for unstructured data like images, audio, and text.

What is a Perceptron?

A Perceptron is the fundamental building block of a neural network. It takes multiple weighted inputs, calculates their sum, adds a bias term, and passes the result through an activation function to produce a binary or continuous output.

Activation Functions Explored

During today's session and coding practices, the following activation functions were explored:

* **ReLU (Rectified Linear Unit):** * *Formula:* $f(x) = \max(0, x)$
* *Common Use:* Used in almost all hidden layers of an ANN to introduce non-linearity and prevent the vanishing gradient problem.


* **Sigmoid:** * *Formula:* $f(x) = \frac{1}{1 + e^{-x}}$
* *Common Use:* Primarily used in the output layer for **Binary Classification** tasks to map values between $0$ and $1$ (representing probabilities).


* **Softmax:** * *Formula:* $f(x_i) = \frac{e^{x_i}}{\sum e^{x_j}}$
* *Common Use:* Used in the output layer for **Multi-class Classification** tasks (like Fashion MNIST) to output a probability distribution across multiple categories.


* **Tanh (Hyperbolic Tangent):**
* *Formula:* $f(x) = \tanh(x)$
* *Common Use:* Used sometimes in hidden layers when the data needs to be centered around $0$ (mapping values between $-1$ and $1$).

 Model Performance & Results

The Artificial Neural Network was trained on the **Fashion MNIST dataset** (60,000 training images, 10,000 testing images of $28 \times 28$ grayscale pixels) for 10 epochs using the `Adam` optimizer and `sparse_categorical_crossentropy` loss.

Final Metrics:

* **Training Accuracy:** ~89.2% (approximate based on execution)
* **Validation Accuracy:** ~87.5%
* **Test Accuracy:** ~86.8%
* **Test Loss:** ~0.36

> **Overfitting Check:** The gap between the training accuracy and the testing accuracy is less than 3% ($<0.05$), indicating a healthy, well-generalized model that is not overfitting.

