from pixel_sampler import PixelSampler
from datetime import datetime

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
    if aa.sampler.args.get_should_generate_image():
            aa.save_ascii_image(f"../data/generated/ascii_art_{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}.png")