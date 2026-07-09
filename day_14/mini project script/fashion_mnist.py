import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Flatten


print("loading fashion mnist dataset...")
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# class names - i looked these up
class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

print("dataset loaded")
print("training images:", X_train.shape)
print("testing images :", X_test.shape)
print("image size     :", X_train.shape[1], "x", X_train.shape[2])
print("total classes  :", len(class_names))

# ---- 2. Explore Dataset ----
print("\nclass distribution in training set:")
for i, name in enumerate(class_names):
    count = (y_train == i).sum()
    print(f"  {i} - {name}: {count} images")

print("\npixel value range before normalization:")
print("min:", X_train.min())
print("max:", X_train.max())

# showing sample images
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(class_names[y_train[i]], fontsize=8)
    plt.axis('off')
plt.suptitle('sample training images', fontsize=12)
plt.tight_layout()
plt.savefig('sample_images.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\nsample images saved as sample_images.png")

# ---- 3. Normalize ----
# dividing by 255 to bring pixel values between 0 and 1
# i think this helps the model train faster and better
X_train = X_train / 255.0
X_test  = X_test / 255.0

print("\nafter normalization:")
print("min:", X_train.min())
print("max:", X_train.max())

# ---- 4. Build ANN ----
print("\nbuilding ann model...")

model = Sequential()

# flatten layer converts 28x28 image to 784 values
# not sure why its needed but without it dense layer wont work on 2d input
model.add(Flatten(input_shape=(28, 28)))

# hidden layer 1 - using relu
# not sure if 128 neurons is right but seems common for mnist
model.add(Dense(units=128, activation='relu'))

# hidden layer 2 - smaller layer
model.add(Dense(units=64, activation='relu'))

# output layer - 10 neurons for 10 classes
# softmax converts to probabilities that add up to 1
model.add(Dense(units=10, activation='softmax'))

print("\nmodel summary:")
model.summary()

# ---- 5. Compile Model ----
# not fully sure about these settings but this is what i found
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
print("\nmodel compiled")
print("optimizer: adam")
print("loss     : sparse categorical crossentropy")

# ---- 6. Train Model ----
print("\ntraining model... this will take a moment")
# using validation_split to monitor overfitting
# keeping epochs low - not sure how many is enough
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

print("\ntraining complete")

# ---- 7. Evaluate ----
print("\nevaluating on test data...")
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
train_acc = history.history['accuracy'][-1]
val_acc   = history.history['val_accuracy'][-1]

print(f"\ntraining accuracy  : {train_acc:.4f}")
print(f"validation accuracy: {val_acc:.4f}")
print(f"test accuracy      : {test_acc:.4f}")
print(f"test loss          : {test_loss:.4f}")

# checking for overfitting
if train_acc - test_acc > 0.05:
    print("\nnote: possible overfitting - train acc much higher than test")
else:
    print("\ntrain and test accuracy close - model looks okay")

# ---- 8. Plot Training Curves ----
plt.figure(figsize=(10, 4))

# accuracy plot
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='val accuracy')
plt.title('training vs validation accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

# loss plot
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.title('training vs validation loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.tight_layout()
plt.savefig('training_curves.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\ntraining curves saved as training_curves.png")

# ---- 9. Make Predictions ----
print("\nmaking predictions on test images...")
predictions = model.predict(X_test, verbose=0)

# showing first 10 predictions
print("\nfirst 10 predictions:")
print(f"{'actual':<20} {'predicted':<20} {'correct?'}")
print("-" * 55)
for i in range(10):
    actual    = class_names[y_test[i]]
    predicted = class_names[np.argmax(predictions[i])]
    correct   = "Yes" if y_test[i] == np.argmax(predictions[i]) else "No"
    print(f"{actual:<20} {predicted:<20} {correct}")

# ---- 10. Sample Prediction Images ----
plt.figure(figsize=(12, 5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[i], cmap='gray')
    predicted = class_names[np.argmax(predictions[i])]
    actual    = class_names[y_test[i]]
    color     = 'green' if predicted == actual else 'red'
    plt.title(f"pred: {predicted}\nactual: {actual}",
              fontsize=7, color=color)
    plt.axis('off')
plt.suptitle('sample predictions (green=correct red=wrong)', fontsize=11)
plt.tight_layout()
plt.savefig('sample_predictions.png')
plt.show(block=False)
plt.pause(3)
plt.close()
print("\nsample predictions saved as sample_predictions.png")

# ---- 11. Final Summary ----
print("\n---- final summary ----")
print(f"dataset         : fashion mnist")
print(f"training samples: {len(X_train)}")
print(f"testing samples : {len(X_test)}")
print(f"model layers    : flatten + dense(128) + dense(64) + dense(10)")
print(f"activation      : relu (hidden) + softmax (output)")
print(f"epochs          : 10")
print(f"train accuracy  : {train_acc:.4f}")
print(f"test accuracy   : {test_acc:.4f}")
print(f"saved files     : sample_images.png, training_curves.png, sample_predictions.png")