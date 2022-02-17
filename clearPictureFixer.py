from PIL import Image
import numpy as np
import os
from glob import glob


def fix_image(file):
    im = Image.open(file)
    im = im.convert('RGBA')


    data = np.array(im)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

    #find clear pixel
    white_areas = (red == 0) & (blue == 0) & (green == 0) & (alpha == 0)
    data[..., :][white_areas.T] = (255, 255, 255, 1) # Transpose back needed

    im2 = Image.fromarray(data)
    im2.save(file)
    print(file)


files = []
start_dir = os.getcwd()
pattern   = "*.png"

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern)))

for file in files:
    fix_image(file)
