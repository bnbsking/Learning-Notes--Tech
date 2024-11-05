import tensorflow as tf
from tensorflow.keras import Input, layers, Model, utils
from tensorflow.keras import optimizers, losses, metrics, callbacks
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

df = pd.read_csv('pokemon-challenge/pokemon.csv')
df.head()

df = df.set_index("#") # set "#" as index
df.head()

df.info() # make up missing data: name and type2

df["Type 2"].fillna('empty', inplace=True)
df.head()

dc = pd.read_csv('pokemon-challenge/combats.csv')
dc.head()

dc['Winner'] = dc.apply(lambda x:0 if x.Winner == x.First_pokemon else 1, axis="columns")
dc.head()

print(dc.dtypes, "\n", "-"*30+"\n", df.dtypes)

# Data preprocessing
# 1 transfer data type and do one-hot encoding
df['Type 1'] = df['Type 1'].astype('category')
df['Type 2'] = df['Type 2'].astype('category')
df['Legendary'] = df['Legendary'].astype('int')
df_type1OneHot = pd.get_dummies(df['Type 1'])
df_type2OneHot = pd.get_dummies(df['Type 2'])
combine_df_OneHot = df_type1OneHot.add(df_type2OneHot, fill_value=0).astype('int64')
df = df.join(combine_df_OneHot)
df.drop("Type 1", axis='columns', inplace=True)
df.drop("Type 2", axis='columns', inplace=True)
df.drop("Name", axis='columns', inplace=True)

pd.options.display.max_columns = 30
df.head()

# dict(enumerate(df['Type 2'].cat.categories))
# df['Type 1'] = df['Type 1'].cat.codes
# df['Type 2'] = df['Type 2'].cat.codes

print("df.shape={}".format(df.shape), "dc.shape={}".format(dc.shape))

# 5 split data into training, validation and testing
n = dc.shape[0]
index = np.random.permutation(n)
train, val, test = dc.loc[index[:int(n*0.6)]], dc.loc[index[int(n*0.6):int(n*0.8)]], dc.loc[index[int(n*0.8):]]

print(train)

# 6 normalization for training and validation
mean = df.loc[:, 'HP':'Generation'].mean() #loc[row,column]
std = df.loc[:, 'HP':'Generation'].std()
df.loc[:, 'HP':'Generation'] = ( df.loc[:, 'HP':'Generation'] - mean )/std

print(df.head())

# 7 numpy form
xTrainIndex = np.array(train.drop('Winner', axis='columns'))
xValIndex = np.array(val.drop('Winner', axis='columns'))
xTestIndex = np.array(test.drop('Winner', axis='columns'))

npData = np.array(df.loc[:, 'HP':])
xTrain, yTrain = npData[xTrainIndex-1].reshape((-1,54)), np.array(train['Winner'])
xVal, yVal = npData[xValIndex-1].reshape((-1,54)), np.array(val['Winner'])
xTest, yTest = npData[xTestIndex-1].reshape((-1,54)), np.array(test['Winner'])

print(xTrain.shape, yTrain.shape)
#nd.array-const substract all indices
#-1 in reshape means ignore, 54 in reshape due to 27*2

inputs = Input(shape=(54,))
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dropout(0.3)(x)
x = layers.Dense(64, activation='relu')(x)
x = layers.Dropout(0.3)(x)
x = layers.Dense(64, activation='relu')(x)
x = layers.Dropout(0.3)(x)
x = layers.Dense(16, activation='relu')(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(1, activation='sigmoid')(x)

myModel = Model(inputs=inputs, outputs=outputs)
myModel.summary()

myModel.compile(optimizers.Adam(0.001), loss=losses.BinaryCrossentropy(), metrics=[metrics.BinaryAccuracy()])
try:
    os.makedirs("lab2-logs/models/")
except:
    pass
log_dir = os.path.join("lab2-logs","model-1")
myModel_cbk = callbacks.TensorBoard(log_dir=log_dir)
myModel_mckp = callbacks.ModelCheckpoint("lab2-logs/models/"+"/Best-model-1.h5", monitor="val_binary_accuracy",\
                                         save_best_only=True, mode="max")
                                         
 history = myModel.fit(xTrain, yTrain, batch_size=64, epochs=200, validation_data=(xVal,yVal), callbacks=[myModel_cbk,myModel_mckp])
 
plt.plot(history.history['binary_accuracy'], label='model-training')
plt.plot(history.history['val_binary_accuracy'], label='model-training')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()

myModel.load_weights( "lab2-logs/models/" + "/Best-model-1.h5" )
loss, accuracy = myModel.evaluate(xTest, yTest)
print("accuracy={:.3f}%".format(accuracy*100))

venusaur = np.expand_dims(npData[3], axis=0) #妙花娃
charizard = np.expand_dims(npData[7], axis=0) #噴火龍
blastoise = np.expand_dims(npData[12], axis=0) #水箭龜

pred1 = myModel.predict(np.concatenate([venusaur,charizard], axis=-1))
pred2 = myModel.predict(np.concatenate([charizard,blastoise], axis=-1))
pred3 = myModel.predict(np.concatenate([blastoise,venusaur], axis=-1))

print("prob of venusaur loses charizard = {}".format(pred1))
print("prob of charizard loses blastoise = {}".format(pred2))
print("prob of blastoise loses venusaur = {}".format(pred3))
