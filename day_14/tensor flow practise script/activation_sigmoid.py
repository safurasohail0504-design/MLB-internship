import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings('ignore')
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
print("building model with sigmoid activation")
model = Sequential()
model.add(Dense(units=16, activation='sigmoid', input_shape=(4,)))
model.add(Dense(units=8, activation='sigmoid'))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()
print("\nsigmoid used in all layers here")
print("output between 0 and 1 for every neuron")
print("not ideal for hidden layers - can cause vanishing gradient")
print("total parameters:", model.count_params())