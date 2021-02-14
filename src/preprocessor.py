import cv2
import matplotlib.pyplot as plt

class Preprocessor:
    def __init__(self):
        self.image_target_size = (28, 28)
        
    def pad_image(self, image):
        padded_image = None
        img_size = image.shape
        top = 0
        bottom = 0
        left = 0
        right = 0
        borderType = cv2.BORDER_CONSTANT
        if img_size[0] > img_size[1]:
            left = int((img_size[0] - img_size[1]) / 2)
            right = int((img_size[0] - img_size[1]) / 2)
        else:
            top = int((img_size[1] - img_size[0]) / 2)
            bottom = int((img_size[1] - img_size[0]) / 2)
        padded_image = cv2.copyMakeBorder(image, top, bottom, left, right, borderType)
        return padded_image
    
    def resize(self, image):
        return cv2.resize(image, self.image_target_size)
    
    def preprocess(self, image):
        padded_image = self.pad_image(image)
        preprocessed_image = self.resize(padded_image)
        return preprocessed_image