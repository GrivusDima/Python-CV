import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv("data/figures.csv")
print(df.head())

encoder = LabelEncoder()
df['label_enc'] = encoder.fit_transform(df['label'])

X = df[['area', 'perimeter', 'corners']]
y = df['label_enc']

model = keras.Sequential([layers.Input(shape=(3,)),
                          layers.Dense(3, activation ='relu'),
                          layers.Dense(3, activation ='relu'),
                          layers.Dense(3, activation ='softmax')])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X, y, epochs = 200, verbose = 0)

plt.plot(history.history['loss'], label='LOSSES')
plt.plot(history.history['accuracy'], label='ACCURACY')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.title('Model Learning Process')
plt.legend()
plt.show()

test = np.array([[42, 26, 4]])

pred = model.predict(test)

print(f'Probability of each class: {pred}')
print(f'Result: {encoder.inverse_transform([np.argmax(pred)])}')