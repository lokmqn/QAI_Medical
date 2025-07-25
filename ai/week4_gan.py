# ai/week4_gan.py
import tensorflow as tf

def build_generator():
    return tf.keras.Sequential([
        tf.keras.layers.Input(shape=(100,)),
        tf.keras.layers.Dense(16*16*3, activation='relu'),
        tf.keras.layers.Reshape((16,16,3)),
        tf.keras.layers.Conv2DTranspose(3, 3, activation='tanh', padding='same')
    ])

def build_discriminator():
    return tf.keras.Sequential([
        tf.keras.layers.Input(shape=(16,16,3)),
        tf.keras.layers.Conv2D(8, 3, activation='relu'),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
  
