import numpy as np
from args_parser import ArgsParser
from image_generator import ImageGenerator
from pixel_sampler import PixelSampler

class AsciiArt:

    def __init__(self, args=None):
        self.sampler = PixelSampler(args)

    def print_ascii_image(self):
        for row in self.sampler.get_ascii_image():
            print(row)

    def save_ascii_image(self, path):
        image = self.sampler.image_generator.text_to_image()
        image.save(path)



if __name__ == "__main__":
    aa = AsciiArt()
    aa.print_ascii_image()
    # aa.save_ascii_image("ascii_art.png")