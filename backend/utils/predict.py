import gdown
import os
import tensorflow as tf

model_path = "model.keras"

if not os.path.exists(model_path):
    url = "https://drive.google.com/uc?id=10hwfSimGop7IXd91FlPjozuTTLgle_Mp"
    gdown.download(url, model_path, quiet=False)

model = tf.keras.models.load_model(model_path, compile=False)