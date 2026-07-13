import tensorflow as tf
from tensorflow.keras import layers, models

print("Loading pre-trained MobileNetV2")
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(160, 160, 3), include_top=False, weights="imagenet"
)
base_model.trainable = False
print("\nBase Model Summary")
base_model.summary()
model = models.Sequential(
    [
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(64, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ]
)
model.compile(
    optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
)
print("\n Model Summary")
model.summary()