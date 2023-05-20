import numpy as np
from args_parser import ArgsParser
from PIL import Image, ImageDraw, ImageFont
from math import ceil

class AsciiArt:

    def __init__(self, args=None):
        self.args = ArgsParser(args)

    def print_ascii_image(self):
        for row in self.get_ascii_image():
            print("".join(row))

    def save_ascii_image(self, path):
        # with open(path, "w") as f:
        #     for row in self.get_ascii_image():
        #         f.write("".join(row) + "\n")
        image = self.text_to_image(["".join(row) for row in self.get_ascii_image()])
        image.save(path)

    def text_to_image(self, lines):
        """Convert text file to a grayscale image.

        arguments:
        textfile_path - the content of this file will be converted to an image
        font_path - path to a font file (for example impact.ttf)
        """
        # parse the file into lines stripped of whitespace on the right side
        # with open(textfile_path) as f:
        #     lines = tuple(line.rstrip() for line in f.readlines())
        COMMON_MONO_FONT_FILENAMES = [
            'DejaVuSansMono.ttf',  # Linux
            'Consolas Mono.ttf',   # MacOS, I think
            'Consola.ttf',         # Windows, I think
        ]
        PIL_GRAYSCALE = 'L'
        PIL_WIDTH_INDEX = 0
        PIL_HEIGHT_INDEX = 1

        # choose a font (you can see more detail in the linked library on github)
        font = None
        large_font = 20  # get better resolution with larger size
        for font_filename in COMMON_MONO_FONT_FILENAMES:
            try:
                font = ImageFont.truetype(font_filename, size=large_font)
                print(f'Using font "{font_filename}".')
                break
            except IOError:
                print(f'Could not load font "{font_filename}".')
        if font is None:
            font = ImageFont.load_default()
            print('Using default font.')

        # make a sufficiently sized background image based on the combination of font and lines
        font_points_to_pixels = lambda pt: round(pt * 96.0 / 72)
        margin_pixels = 20

        # height of the background image
        tallest_line = max(lines, key=lambda line: font.getsize(line)[PIL_HEIGHT_INDEX])
        max_line_height = font_points_to_pixels(font.getsize(tallest_line)[PIL_HEIGHT_INDEX])
        realistic_line_height = max_line_height * 0.8  # apparently it measures a lot of space above visible content
        image_height = int(ceil(realistic_line_height * len(lines) + 2 * margin_pixels))

        # width of the background image
        widest_line = max(lines, key=lambda s: font.getsize(s)[PIL_WIDTH_INDEX])
        max_line_width = font_points_to_pixels(font.getsize(widest_line)[PIL_WIDTH_INDEX])
        image_width = int(ceil(max_line_width + (2 * margin_pixels)))

        # draw the background
        background_color = 0  # white
        image = Image.new(PIL_GRAYSCALE, (image_width, image_height), color=background_color)
        draw = ImageDraw.Draw(image)

        # draw each line of text
        font_color = 255  # black
        horizontal_position = margin_pixels
        for i, line in enumerate(lines):
            vertical_position = int(round(margin_pixels + (i * realistic_line_height)))
            draw.text((horizontal_position, vertical_position), line, fill=font_color, font=font)

        return image

    def get_ascii_image(self):
        img_arr = self.args.get_resized_bw_img()
        charset = self.args.get_charset()

        ptgs = self.get_ptgs(len(charset))
        ascii_arr = [[" " for _ in range(img_arr.shape[1])] for _ in range(img_arr.shape[0])]

        for i, ptg in enumerate(ptgs):
            last_ptg = ptgs[i-1] if i > 0 else 0

            lt_idxs = self.tuple_set(np.argwhere(img_arr < ptg * 255).tolist())
            gt_idxs = self.tuple_set(np.argwhere(img_arr >= last_ptg * 255).tolist())

            idxs = list(set(lt_idxs).intersection(gt_idxs))
            for idx in idxs:
                ascii_arr[idx[0]][idx[1]] = charset[i]*2
        
        return ascii_arr

    def get_ptgs(self, n):
        sampler = self.args.get_sampler()
        lower_ptg = self.args.get_lower_ptg()
        upper_ptg = self.args.get_upper_ptg()

        if sampler == "linear":
            return [0] + np.linspace(lower_ptg, upper_ptg, n-2).tolist() + [1]
        elif sampler == "log":
            return np.logspace(lower_ptg, upper_ptg, n-1).tolist() + [1]
        elif sampler == "exp":
            return np.exp(np.linspace(lower_ptg, upper_ptg, n-1)).tolist() + [1]
        else:
            raise ValueError("Invalid sampler.")

    def tuple_set(self, seq):
        return {tuple(item) for item in seq}


if __name__ == "__main__":
    aa = AsciiArt()
    aa.print_ascii_image()
    aa.save_ascii_image("ascii_art.png")