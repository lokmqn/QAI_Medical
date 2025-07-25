# ai/week1_classifier.py
import tensorflow as tf

def build_model():
    return tf.keras.Sequential([
        tf.keras.layers.Input(shape=(224,224,3)),
        tf.keras.layers.Conv2D(8, 3, activation='relu'),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(3, activation='softmax')
    ])

if __name__ == "__main__":
    model = build_model()
    model.summary()
