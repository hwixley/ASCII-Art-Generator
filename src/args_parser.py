import os, sys, re
from PIL import Image
import numpy as np
from constants import VERSION

class ArgsParser:

    CHARSETS = {
        "tiny": " .~+=@#",
        "small": " .:-=+*#%@",
        "medium": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{\}[]?-_+~<>i!lI;:,\"^`'."[::-1],
        "large": "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi\{C\}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    }
    SAMPLERS = ["linear", "log", "exp"]
    ALL_ARGS = ["-h", "--help", "-v", "--version", "-i", "--img", "-c", "--charset", "-s", "--sampler", "-l", "--lower-ptg", "-u", "--upper-ptg", "-w", "--img-width", "-g", "--gen-img"]

    def __init__(self, args=sys.argv):
        self.args = args or sys.argv

    def get(self, arg_name, default, has_value):
        if not has_value:
            return arg_name in self.args
        try:
            arg_idx = self.args.index(arg_name)
            return self.args[arg_idx + 1]
        except ValueError:
            return default
        
    def get_arg(self, short, long, default, has_value=True):
        return self.get(short, default, has_value) or self.get(long, default, has_value)
        
    def get_resized_bw_img(self):
        DEFAULT_IMG = f"{os.path.dirname(os.path.realpath(__file__))}/../data/cage.jpg"
        img_path = self.get_arg("-i", "--img", DEFAULT_IMG)
        new_width = self.get_img_width()

        if not os.path.exists(img_path):
            if os.path.exists(f"{os.getcwd()}/{img_path}"):
                img_path = f"{os.getcwd()}/{img_path}"
            else:
                print("Invalid image path. Using default image.")
                img_path = DEFAULT_IMG
        img = Image.open(img_path).convert('L')
        ratio = img.size[0] / img.size[1]
        height = int(new_width / ratio)
        if height < 1:
            new_width = int(new_width * ratio)
            height = 1
        img = img.resize((new_width, height))
        return np.array(img)
        
    def get_charset(self):
        DEFAULT_CHARSET = "small"
        val = self.get_arg("-c", "--charset", DEFAULT_CHARSET)

        if val not in self.CHARSETS.keys():
            print("Invalid charset. Using default charset.")
            return self.CHARSETS[DEFAULT_CHARSET]
        else:
            return self.CHARSETS[val]
        
    def get_sampler(self):
        DEFAULT_SAMPLER = "linear"
        val = self.get_arg("-s", "--sampler", DEFAULT_SAMPLER)

        if val not in self.SAMPLERS:
            print("Invalid sampler. Using default sampler.")
            return DEFAULT_SAMPLER
        else:
            return val
    
    def get_lower_ptg(self):
        DEFAULT_LOWER_PTG = 0.2
        val = float(self.get_arg("-l", "--lower-ptg", DEFAULT_LOWER_PTG))

        if val < 0 or val > 1:
            print("Invalid lower percentage. Using default lower percentage.")
            return DEFAULT_LOWER_PTG
        else:
            return val
            
    
    def get_upper_ptg(self):
        DEFAULT_UPPER_PTG = 0.4
        val = float(self.get_arg("-u", "--upper-ptg", DEFAULT_UPPER_PTG))

        if val < 0 or val > 1:
            print("Invalid upper percentage. Using default upper percentage.")
            return DEFAULT_UPPER_PTG
        else:
            return val
        
    def get_img_width(self):
        DEFAULT_IMG_WIDTH = 80
        val = int(self.get_arg("-w", "--img-width", DEFAULT_IMG_WIDTH))

        if val <= 0:
            print("Invalid image width. Using default image width.")
            return DEFAULT_IMG_WIDTH
        else:
            return val
        
    def get_should_generate_image(self):
        val = self.get_arg("-g", "--gen-img", False, False)
        return val
        
    def check_for_invalid_args(self):
        if self.get_arg("-h", "--help", None, False):
            print("Usage: python ascii_art.py [options]")
            print("Options:")
            arg_strs =  "".join([f" , {arg}\n" if len(arg) > 1 and arg[:2] == "--" else arg for arg in self.ALL_ARGS])
            print(arg_strs)
            sys.exit(0)
        elif self.get_arg("-v", "--version", None, False):
            print(f"Version: {VERSION}")
            sys.exit(0)
        else:
            arg_regex = re.compile(r"^-")
            bad_args = [arg for arg in self.args if arg_regex.match(arg) and not arg in self.ALL_ARGS]

            if len(bad_args) > 0:
                bad_args_str = "\"" + "\" , \"".join(bad_args) + "\""
                print(f"You have entered invalid arguments:\n{bad_args_str}\n\nUse -h or --help to see the available arguments and their notations.")
                sys.exit(1)