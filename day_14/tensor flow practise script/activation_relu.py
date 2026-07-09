import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings('ignore')
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
print("building model with relu activation")
model = Sequential()
model.add(Dense(units=16, activation='relu', input_shape=(4,)))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()
print("\nrelu is used in hidden layers")
print("relu helps avoid vanishing gradient problem i think")
print("total parameters:", model.count_params())