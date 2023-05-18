import numpy as np
from PIL import Image
import sys

args = sys.argv

def tuple_set(seq):
    return {tuple(item) for item in seq}

img = Image.open('../data/fractal.webp').convert('L')

ratio = img.size[0] / img.size[1]
new_width = 80
img = img.resize((new_width, int(new_width / ratio)))

img_arr = np.array(img)
img.save('greyscale.png')

bw = False
ascii_print = True

if bw:
    ptg = 0.28
    img_arr[img_arr < ptg * 255] = 0
    img_arr[img_arr >= ptg * 255] = 255
else:
    charset1 = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi\{C\}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    charset2 = " .~+=@#"
    charset3 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{\}[]?-_+~<>i!lI;:,\"^`'."
    charset4 = " .:-=+*#%@"
    charset = charset1
    ptg_types = ["linear", "log", "exp"]
    ptg_type = ptg_types[0]
    min_ptg = float(args[1]) if len(args) > 1 else 0.1
    max_ptg = float(args[2]) if len(args) > 2 else 0.5
    ptgs = np.empty(len(charset))
    if ptg_type == "linear":
        ptgs = [0] + np.linspace(min_ptg, max_ptg, len(charset)-2).tolist() + [1]
    elif ptg_type == "log":
        ptgs = np.logspace(min_ptg, np.log10(max_ptg), len(charset)-1).tolist() + [1]
    elif ptg_type == "exp":
        ptgs = np.exp(np.linspace(min_ptg, np.log(max_ptg), len(charset)-1)).tolist() + [1]

    ascii_arr = [[" " for _ in range(img_arr.shape[1])] for _ in range(img_arr.shape[0])]

    for i, ptg in enumerate(ptgs):
        last_ptg = ptgs[i-1] if i > 0 else 0
        lt_idxs = tuple_set(np.argwhere(img_arr < ptg * 255).tolist())
        gt_idxs = tuple_set(np.argwhere(img_arr >= last_ptg * 255).tolist())

        idxs = list(set(lt_idxs).intersection(gt_idxs))

        for idx in idxs:
            ascii_arr[idx[0]][idx[1]] = charset[i]*2

if ascii_print:
    for row in ascii_arr:
        print("".join(row))

img2 = Image.fromarray(img_arr)
img2.save('greyscale2.png')