import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings('ignore')
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
print("building model with tanh activation")
model = Sequential()
model.add(Dense(units=16, activation='tanh', input_shape=(4,)))
model.add(Dense(units=8, activation='tanh'))
model.add(Dense(units=1, activation='sigmoid'))  
model.summary()
print("\ntanh used in hidden layers")
print("output between -1 and 1 - centered at zero")
print("sigmoid still used in output layer for binary classification")
print("total parameters:", model.count_params())