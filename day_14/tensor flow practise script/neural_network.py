import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense

# Define the sequential model
model = Sequential()
model.add(Dense(units=8, activation='relu', input_shape=(4,)))
model.add(Dense(units=1, activation='sigmoid'))

print("model summary:")
model.summary()

print("\nlayer details:")
for i, layer in enumerate(model.layers):
    print(f"layer {i+1}: {layer.name}")
    print(f"   type : {type(layer).__name__}")
    # Fixed here: Changed layer.output_shape to layer.output.shape
    print(f"   output : {layer.output.shape}")
    print(f"   parameters: {layer.count_params()}")