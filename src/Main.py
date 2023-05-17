import numpy as np
from PIL import Image

img = Image.open('../data/cage.jpg').convert('L')

img_arr = np.array(img)

img.save('greyscale.png')

# ptgs = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
ptg = 0.28

# for i, ptg in enumerate(ptgs[1:]):
#     val = i+1/len(ptgs) * 255
#     if i == len(ptgs) - 2:
#         img_arr[img_arr >= ptg * 255] = val
#     else:
#         img_arr[img_arr < ptg * 255] = val
#         img_arr[img_arr >= ptg * 255] = val

img_arr[img_arr < ptg * 255] = 0

img_arr[img_arr >= ptg * 255] = 255

img2 = Image.fromarray(img_arr)

img2.save('greyscale2.png')