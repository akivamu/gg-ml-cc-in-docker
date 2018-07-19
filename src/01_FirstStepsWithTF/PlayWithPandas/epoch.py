import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.data import Dataset


total_rooms = pd.Series([1, 2, 3])
random_nums = pd.Series([11, 22, 33])
median_house_value = pd.Series([1000, 1500, 1700])
dataFrame = pd.DataFrame({
     'total_rooms': total_rooms, 
     'random_nums': random_nums, 
     'median_house_value': median_house_value})

features = {key:np.array(value) for key,value in dict(dataFrame[['total_rooms', 'random_nums']]).items()}
targets = dataFrame['median_house_value']

ds = Dataset.from_tensor_slices((features,targets))

print "---- Original dataset"
iter = ds.make_one_shot_iterator()
session = tf.Session()
while True:
  try:
    print(session.run(iter.get_next()))
  except tf.errors.OutOfRangeError:
    break

print "---- Batch = 2"
batchedDs = ds.batch(2)
iter = batchedDs.make_one_shot_iterator()
session = tf.Session()
while True:
  try:
    print(session.run(iter.get_next()))
  except tf.errors.OutOfRangeError:
    break

print "---- Batch = 2, Epochs = 3"
epochBatchedDs = ds.batch(2).repeat(3)
iter = epochBatchedDs.make_one_shot_iterator()
session = tf.Session()
while True:
  try:
    print(session.run(iter.get_next()))
  except tf.errors.OutOfRangeError:
    break
