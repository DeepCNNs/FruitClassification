# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow.keras import models

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import enum
from src.common import FruitType
from src.preprocessor import Preprocessor

import cv2

class Classifier:
    # initialize model and preprocessor objects
    def __init__(self, model_path):
        self.model = models.load_model(model_path)
        self.pprocessor = Preprocessor()
        
    def predict(self, image):
        # preproced the image before inference
        padded_image = self.pprocessor.preprocess(image)
        test_image = np.expand_dims(padded_image, axis=0)
        
        # predict fruit type using trained model
        pred = self.model.predict(test_image)
        return self.get_class_string(pred[0])
        
    # converts the result to fruit identifier
    def get_class_string(self, pred_list):
        identifier = 0
        max_score = 0
        i = 0
        
        for pred in pred_list:
            if pred > max_score:
                max_score = pred
                identifier = i
            i += 1
        return FruitType(identifier).name