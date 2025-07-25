# ai/week2_train.py
import tensorflow as tf
from ai.week1_classifier import build_model

model = build_model()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# dummy data
x = tf.random.normal((20, 224, 224, 3))
y = tf.keras.utils.to_categorical(tf.random.uniform((20,), maxval=3), 3)
model.fit(x, y, epochs=2)
