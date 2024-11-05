import tensorflow as tf
from tensorflow.keras import Input, layers, Model, utils

imageInput = Input(shape=(128,128,3))
h1 = layers.Conv2D(64, 5, 2, activation="relu")(imageInput)
h2 = layers.Conv2D(32, 5, 2, activation="relu")(h1)
h3 = layers.Conv2D(32, 5, 2, activation="relu")(h2)
hf = layers.Flatten()(h3)

infoInput = Input(shape=(10,))
h4 = layers.Dense(64)(infoInput)

conc = layers.Concatenate()([hf,h4])

output1 = layers.Dense(1)(conc)
output2 = layers.Dense(1)(conc)
output3 = layers.Dense(1)(conc)

myModel = Model(inputs=[imageInput, infoInput], outputs=[output1, output2, output3])
utils.plot_model(myModel, to_file = "temp.png")

myModel.summary()

