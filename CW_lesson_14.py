import os
import numpy as np
import tensorflow as tf
import keras
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image


BASE_DIR = os.path.dirname(__file__)
TRAIN_PATH = os.path.join(BASE_DIR, 'data', 'train')
TEST_PATH = os.path.join(BASE_DIR, 'data', 'test')


train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    TRAIN_PATH, image_size=(128, 128), batch_size=20,
    label_mode='categorical'
)
test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    TEST_PATH, image_size=(128, 128), batch_size=20,
    label_mode='categorical'
)

model = models.Sequential()
model.add(keras.Input(shape=(128, 128, 3)))
model.add(layers.Rescaling(1./255))

#first layer
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2))) #MaxPooling() gets rid of secondary elements, leaving only the main one

#second layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

#second layer
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu')) # This is a hidden layer
model.add(layers.Dense(6, activation='softmax')) # The actual output layer


model.compile(
    optimizer='adam', #the type of learning(teaching), in this case - show and tell
    loss = 'categorical_crossentropy',
    metrics = ['accuracy'])

model.fit(train_ds, epochs=24, validation_data=test_ds)

test_photo = os.path.join(BASE_DIR, 'images', "test.format")

if os.path.exists(test_photo):
    img = image.load_img(test_photo, target_size=(128, 128))
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0) #  a batch dimension so the shape becomes (1, 128, 128, 3)

    predictions = model.predict(img_array)
    class_name = sorted(os.listdir(TRAIN_PATH))

    result_ind = np.argmax(predictions[0])

    print(f'Result: {class_name[result_ind]}')