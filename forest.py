import numpy as np
from keras.layers import *
from keras.models import Sequential

data_set = np.loadtxt('data/covtype.data', delimiter=',')
forest_type_index = 54
Y = data_set[:, forest_type_index]
X = data_set[:, 0:forest_type_index]
list_by_forest_types = [data_set[data_set[:, forest_type_index] == i] for i in range(1, 8)]
train_ratio = 0.1
line_size = data_set[0].size
dim = line_size - 1
list_train = [list_by_forest_types[i][0:int(train_ratio * list_by_forest_types[i].size / line_size)] for i in
              range(0, 7)]
data_train = np.asarray(list_train)
data_train = np.concatenate(data_train)
Y_train = data_train[:, forest_type_index]
X_train = data_train[:, 0:forest_type_index]

model = Sequential()
model.add(Dense(dim, input_dim=dim))
model.add(BatchNormalization())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(256))
model.add(Activation('tanh'))
model.add(Dense(7))
model.add(Activation('softmax'))

model.summary()

model.compile(loss='sparse_categorical_crossentropy',
              optimizer="sgd",
              metrics=['accuracy'],
              )
