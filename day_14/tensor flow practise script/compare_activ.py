import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings('ignore')
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
def build_model(activation_name):
    model = Sequential()
    model.add(Dense(units=16,
                    activation=activation_name,
                    input_shape=(4,)))
    model.add(Dense(units=8, activation=activation_name))
    model.add(Dense(units=1, activation='sigmoid'))
    return model
activations = ['relu', 'sigmoid', 'tanh']
for act in activations:
    print(f"\nmodel with {act}")
    model = build_model(act)
    model.summary()
    print(f"total params: {model.count_params()}")
print("\nobservation:")
print("all 3 models have the same number of parameters")
print("activation function only changes how values are processed")
print("not the number of connections or neurons")