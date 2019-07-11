# Explore constant and operator nodes
# How to set up and use nodes
# How to run nodes to output their values

import tensorflow as tf

const_node1 = tf.constant(1.0, dtype=tf.float32)
const_node2 = tf.constant(2.0)

print(const_node1)
print(const_node2)
