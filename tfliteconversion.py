import tensorflow as tf

# make a converter object from the saved tensorflow file
converter = tf.lite.TFLiteConverter.from_saved_model('runs/train/exp14/weights/saved_model')
converter.target_spec.supported_ops = [
  tf.lite.OpsSet.TFLITE_BUILTINS, # enable TensorFlow Lite ops.
  tf.lite.OpsSet.SELECT_TF_OPS # enable TensorFlow ops.
]
# tell converter which type of optimization techniques to use
converter.optimizations = [tf.lite.Optimize.DEFAULT]
# to view the best option for optimization read documentation of tflite about optimization
# go to this link https://www.tensorflow.org/lite/guide/get_started#4_optimize_your_model_optional

# convert the model 
tf_lite_model = converter.convert()
# save the converted model 
open('best.tflite', 'wb').write(tf_lite_model)
