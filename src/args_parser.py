import os, sys
from PIL import Image
import numpy as np

class ArgsParser:

    CHARSETS = {
        "tiny": " .~+=@#",
        "small": " .:-=+*#%@",
        "medium": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{\}[]?-_+~<>i!lI;:,\"^`'."[::-1],
        "large": "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi\{C\}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    }
    SAMPLERS = ["linear", "log", "exp"]

    def __init__(self):
        self.args = sys.argv
        self.image = None
        self.scaledImage = None

    def get(self, arg_name, default=None):
        try:
            arg_idx = self.args.index(arg_name)
            return self.args[arg_idx + 1]
        except ValueError:
            return default
        
    def get_arg(self, short, long, default=None):
        try:
            return self.get(short, default=default) or self.get(long, default=default)
        except ValueError:
            return None
        
    def get_resized_bw_img(self):
        DEFAULT_IMG = f"{os.path.dirname(os.path.realpath(__file__))}/../data/cage.jpg"
        img_path = self.get_arg("-i", "--img", default=DEFAULT_IMG)
        new_width = self.get_img_width()

        if img_path is None:
            return None
        else:
            if not os.path.exists(img_path):
                if os.path.exists(f"{os.getcwd()}/{img_path}"):
                    img_path = f"{os.getcwd()}/{img_path}"
                else:
                    print("Invalid image path. Using default image.")
                    img_path = DEFAULT_IMG
            self.image = Image.open(img_path).convert('L')
            ratio = self.image.size[0] / self.image.size[1]
            new_height = int(new_width / ratio)
            self.scaledImage = self.image.resize((new_width, new_height))
            return np.array(self.scaledImage)
        
    def get_charset(self):
        DEFAULT_CHARSET = "small"
        val = self.get_arg("-c", "--charset", default=DEFAULT_CHARSET)

        if val is None:
            return self.CHARSETS[DEFAULT_CHARSET]
        elif val not in self.CHARSETS.keys():    
            print("Invalid charset. Using default charset.")
            return self.CHARSETS[DEFAULT_CHARSET]
        else:
            return self.CHARSETS[val]
        
    def get_sampler(self):
        DEFAULT_SAMPLER = "linear"
        val = self.get_arg("-s", "--sampler", default=DEFAULT_SAMPLER)

        if val is None:
            return DEFAULT_SAMPLER
        elif val not in self.SAMPLERS:
            print("Invalid sampler. Using default sampler.")
            return DEFAULT_SAMPLER
        else:
            return val
    
    def get_lower_ptg(self):
        DEFAULT_LOWER_PTG = 0.2
        val = float(self.get_arg("-l", "--lower-ptg", default=DEFAULT_LOWER_PTG))

        if val is None:
            return DEFAULT_LOWER_PTG
        elif val < 0 or val > 1:
            print("Invalid lower percentage. Using default lower percentage.")
            return DEFAULT_LOWER_PTG
        else:
            return val
            
    
    def get_upper_ptg(self):
        DEFAULT_UPPER_PTG = 0.4
        val = float(self.get_arg("-u", "--upper-ptg", default=DEFAULT_UPPER_PTG))

        if val is None:
            return DEFAULT_UPPER_PTG
        elif val < 0 or val > 1:
            print("Invalid upper percentage. Using default upper percentage.")
            return DEFAULT_UPPER_PTG
        else:
            return val
        
    def get_img_width(self):
        DEFAULT_IMG_WIDTH = 80
        val = int(self.get_arg("-w", "--img-width", default=DEFAULT_IMG_WIDTH))

        if val is None:
            return DEFAULT_IMG_WIDTH
        elif val <= 0:
            print("Invalid image width. Using default image width.")
            return DEFAULT_IMG_WIDTH
        else:
            return val     

    def get_img_height(self):
        if self.scaledImage is None:
            self.get_resized_bw_img()
        
        return self.scaledImage.size[1]


    def get_ascii_pixel_size(self):
        width = self.get_img_width()
        height = self.get_img_height()
        ratio = width / height

        multipliers = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
        for i, mult in enumerate(multipliers):
            if width <= mult:
                cols = i + 2
                rows = int(cols / ratio)
                return (rows, cols)