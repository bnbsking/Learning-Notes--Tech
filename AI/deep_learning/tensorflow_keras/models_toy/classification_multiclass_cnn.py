import tensorflow as tf 
import tensorflow_datasets as tfds

train = tfds.load("mnist", split=tfds.Split.TRAIN)
train = train.shuffle(1024).batch(32).prefetch(tf.data.experimental.AUTOTUNE)

# myModel.fit(train, epochs=100)

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from tensorflow.keras import Input, layers, Model, utils
from tensorflow.keras import optimizers, losses, metrics, callbacks

validSplit, trainSplit = tfds.Split.TRAIN.subsplit([10,90])
trainData, info = tfds.load("cifar10", split=trainSplit, with_info=True)
valData = tfds.load("cifar10", split=validSplit)
testData = tfds.load("cifar10", split=tfds.Split.TEST)

print(info)

labels_dict = dict(enumerate(info.features['label'].names))
labels_dict

trainDict = {}
for data in trainData:
    label = data['label'].numpy()
    #print(label)
    trainDict[label] = trainDict.setdefault(label, 0) + 1
print(trainDict)

output = np.zeros((32*8,32*8,3), dtype=np.uint8)
row = 0
for data in trainData.batch(8).take(8):
    output[:, row*32:(row+1)*32] = np.vstack(data['image'].numpy())
    row+=1
plt.figure(figsize=(8,8))
plt.imshow(output)

def parse_fn(dataset):
    x = tf.cast(dataset['image'], tf.float32)/255
    y = tf.one_hot(dataset['label'], 10)
    return x,y
    
AUTOTUNE = tf.data.experimental.AUTOTUNE
batch_size = 64
train_num = int(info.splits['train'].num_examples/10)*9

trainData = trainData.shuffle(train_num)
trainData = trainData.map(map_func=parse_fn, num_parallel_calls=AUTOTUNE)
trainData = trainData.batch(batch_size).prefetch(buffer_size=AUTOTUNE)

valData = valData.map(map_func=parse_fn, num_parallel_calls=AUTOTUNE)
valData = valData.batch(batch_size).prefetch(buffer_size=AUTOTUNE)

testData = testData.map(map_func=parse_fn, num_parallel_calls=AUTOTUNE)
testData = testData.batch(batch_size).prefetch(buffer_size=AUTOTUNE)

inputs = Input(shape=(32, 32, 3))
x = layers.Conv2D(64, (3,3), activation='relu')(inputs)
x = layers.MaxPool2D()(x)
x = layers.Conv2D(128, (3,3), activation='relu')(x)
x = layers.Conv2D(256, (3,3), activation='relu')(x)
x = layers.Conv2D(128, (3,3), activation='relu')(x)
x = layers.Conv2D(64, (3,3), activation='relu')(x)
x = layers.Flatten()(x)
x = layers.Dense(64, activation='relu')(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(10,activation='softmax')(x)

myModel = Model(inputs, outputs) 
myModel.summary()

myModel.compile(optimizers.Adam(0.001), loss=losses.CategoricalCrossentropy(), metrics=[metrics.CategoricalAccuracy()])
try:
    os.makedirs("lab2-logs/models/")
except:
    pass
log_dir = os.path.join("lab2-logs","model-1")
myModel_cbk = callbacks.TensorBoard(log_dir=log_dir)
myModel_mckp = callbacks.ModelCheckpoint("lab2-logs/models/"+"/Best-model-1.h5", monitor="val_categorical_accuracy",\
                                         save_best_only=True, mode="max")
                                         
history = myModel.fit(trainData, epochs=60, validation_data=valData, callbacks=[myModel_cbk,myModel_mckp])

myModel.load_weights('lab2-logs/models/Best-model-1.h5')
loss, acc = myModel.evaluate(testData)
print("accuracy={}".format(acc))
