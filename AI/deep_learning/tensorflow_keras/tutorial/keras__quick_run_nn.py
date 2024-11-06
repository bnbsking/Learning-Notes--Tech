from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
import numpy as np

xTrain = np.random.random((100000,1024))
yTrain = np.random.random(100000)

inputL = Input(shape=(1024,))
x = Dense(1024, activation='relu')(inputL)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)

model=Model(inputL,x)
model.compile(optimizer="Adam", loss="mse")
model.fit(xTrain, yTrain, epochs=1000)