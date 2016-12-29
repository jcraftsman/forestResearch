import time
import numpy as np
from keras.layers import *
from keras.models import Sequential
from keras.utils import np_utils

start_time = time.time()
data_set = np.loadtxt('data/covtype.data', delimiter=',')
forest_type_index = 54
Y = data_set[:, forest_type_index]
X = data_set[:, 0:forest_type_index]
list_by_forest_types = [data_set[data_set[:, forest_type_index] == i] for i in range(1, 8)]
train_ratio = 0.6
line_size = data_set[0].size
dim = line_size - 1
list_train = [list_by_forest_types[i][0:int(train_ratio * list_by_forest_types[i].size / line_size)] for i in
              range(0, 7)]
data_train = np.asarray(list_train)
data_train = np.concatenate(data_train)
Y_train = data_train[:, forest_type_index]
X_train = data_train[:, 0:forest_type_index]
Y_train = np_utils.to_categorical(np.add(Y_train,-1), 7)
Y = np_utils.to_categorical(np.add(Y,-1), 7)

model = Sequential()
model.add(Dense(512, input_dim=dim, init='he_normal'))
model.add(BatchNormalization())
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(512, init='he_normal'))
model.add(BatchNormalization())
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(7, init='he_normal'))
model.add(BatchNormalization())
model.add(Activation('softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer="adam",
              metrics=['accuracy'],
)                    
            
fitter = model.fit(X_train,Y_train,batch_size=128, nb_epoch=10,
                   verbose=2, validation_data=(X, Y))

elapsed_time = time.time() - start_time
print("Execution time: %.3f sec." % elapsed_time)
