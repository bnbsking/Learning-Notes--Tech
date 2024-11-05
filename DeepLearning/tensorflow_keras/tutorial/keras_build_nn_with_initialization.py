# sigmoid/tanh: Glorot/Xavier initialization
# ReLU He initialization

from tensorflow.keras import initializers

layers.Dense(100, 'relu', False, initializers.glorot_normal()) # default
layers.Dense(100, 'relu', False, initializers.he_normal())
