import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import keras
print("tensorflow version:", tf.__version__)
print("keras version:", keras.__version__)
print("\nnum gpus available:", len(tf.config.list_physical_devices('GPU')))
print("num cpus available:", len(tf.config.list_physical_devices('CPU')))
print("\ntensorflow imported successfully")
print("ready to build neural networks")