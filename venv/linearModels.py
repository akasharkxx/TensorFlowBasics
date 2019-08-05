import tensorflow as tf

# y = Wx + b
# x = [1, 2, 3, 4]
# y = [0, -1, -2, -3]

W = tf.Variable([-.5], dtype=tf.float32)
b = tf.Variable([.5], dtype=tf.float32)

