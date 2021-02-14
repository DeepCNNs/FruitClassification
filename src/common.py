from os import listdir
from os.path import isfile, join
import enum
import cv2

# Read all the files in a directory
def read_files_from_dir(self, mypath):
    allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return allfiles

# Fruit type identifier
class FruitType(enum.Enum):
    APPLE = 0
    BANANA = 1
    ORANGE = 2
    
# read image
def read_image(path):
    image = cv2.imread(path)
    return image

