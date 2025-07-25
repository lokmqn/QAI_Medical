"""
Load 10 medical images from Kaggle
"""
import tensorflow as tf
import tensorflow_datasets as tfds

def load_medical(n=10):
    ds, info = tfds.load('patch_camelyon', split='train', shuffle_files=True, with_info=True)
    images = []
    for sample in ds.take(n):
        img = tf.image.resize(sample['image'], [224, 224]) / 255.0
        label = tf.cast(sample['label'], tf.int32)
        images.append((img.numpy(), int(label)))
    return images
  
