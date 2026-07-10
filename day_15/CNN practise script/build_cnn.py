import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist

# load the data
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# oops forgot to reshape first time, adding it now
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# Normalizing the data (hope this works)
X_train = X_train / 255.0
X_test = X_test / 255.0

# building the cnn model architecloa
# making a simple network to see if it learns anything
model = models.Sequential()

# first conv layer with max pooling
model.add(layers.Conv2D(16, (3, 3), activation="relu", input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# flat layer before dense
model.add(layers.Flatten())

# Beginner Mistake: Forgot to add activation="relu" here!
# This leaves it as a linear layer, lowering final capacity/accuracy.
model.add(layers.Dense(32))

# output layer (10 classes)
model.add(layers.Dense(10, activation="softmax"))

# compiling with default adam optimizer
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

# print summary to check shapes
model.summary()

print("\nstarting the training process")

# Beginner Mistake: Using a huge batch size (256) and low epochs (3).
# This causes fewer gradient updates per epoch, making accuracy climb slowly.
history = model.fit(
    X_train,
    y_train,
    epochs=3,
    batch_size=256,
    validation_split=0.2,  # splitting 20% for val
)

# save it so practice 3 script can find it
model.save("simple_fashion_mnist_cnn.h5")
print("done training, model saved!")