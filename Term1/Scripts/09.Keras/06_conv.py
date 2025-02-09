'''
@Author: Shuai Wang
@Github: https://github.com/wsustcid
@Version: 1.0.0
@Date: 2020-04-07 20:44:10
@LastEditTime: 2020-04-08 16:31:31
'''
# Load pickled data
import pickle
import numpy as np
#import tensorflow as tf
#tf.python.control_flow_ops = tf

with open('./small_traffic_set/small_train_traffic.p', mode='rb') as f:
    data = pickle.load(f)

X_train, y_train= data['features'], data['labels']

# Initial Setup for Keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D

# TODO: Build Convolutional Neural Network in Keras Here
model = Sequential()
model.add(Convolution2D(32,(3,3),
                        padding='valid', 
                        activation='relu',
                        input_shape=(32,32,3)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(5, activation='softmax'))


# Preprocess data
X_normalized = np.array(X_train / 255.0 - 0.5 )

from sklearn.preprocessing import LabelBinarizer
label_binarizer = LabelBinarizer()
y_one_hot = label_binarizer.fit_transform(y_train)

model.compile('adam', 'categorical_crossentropy', ['accuracy'])
history = model.fit(X_normalized, y_one_hot, nb_epoch=3, validation_split=0.2)