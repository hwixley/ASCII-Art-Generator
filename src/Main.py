import numpy as np
from PIL import Image

img = Image.open('../data/cage.jpg').convert('L')
ratio = img.size[0] / img.size[1]
new_width = 80
img = img.resize((new_width, int(new_width / ratio)), Image.ANTIALIAS)

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

for row in img_arr:
    print(",".join(map(str, row)).replace("0", "  ").replace("255", "XX").replace(",", ""))

img2 = Image.fromarray(img_arr)

img2.save('greyscale2.png')