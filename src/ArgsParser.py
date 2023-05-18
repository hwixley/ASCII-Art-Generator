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
        
    def get_bw_image(self, new_width: int = 80):
        img_path = self.get_arg("-i", "--img", default=f"{os.path.dirname(os.path.realpath(__file__))}/../data/cage.jpg")

        if img_path is None:
            return None
        else:
            img = Image.open(img_path).convert('L')
            ratio = img.size[0] / img.size[1]
            img = img.resize((new_width, int(new_width / ratio)))
            return np.array(img)
        
    def get_charset(self):
        DEFAULT_CHARSET = "medium"
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
        DEFAULT_LOWER_PTG = 0.1
        val = float(self.get_arg("-l", "--lower-ptg", default=DEFAULT_LOWER_PTG))
        if val is None:
            return DEFAULT_LOWER_PTG
        elif val < 0 or val > 1:
            print("Invalid lower percentage. Using default lower percentage.")
            return DEFAULT_LOWER_PTG
        else:
            return val
            
    
    def get_upper_ptg(self):
        DEFAULT_UPPER_PTG = 0.5
        val = float(self.get_arg("-u", "--upper-ptg", default=DEFAULT_UPPER_PTG))
        if val is None:
            return DEFAULT_UPPER_PTG
        elif val < 0 or val > 1:
            print("Invalid upper percentage. Using default upper percentage.")
            return DEFAULT_UPPER_PTG
        else:
            return val
        