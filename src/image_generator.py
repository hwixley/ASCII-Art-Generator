from PIL import Image, ImageDraw, ImageFont
from math import ceil

class ImageGenerator:

    COMMON_MONO_FONT_FILENAMES = [
        'DejaVuSansMono.ttf',  # Linux
        'Consolas Mono.ttf',   # MacOS
        'Consola.ttf',         # Windows
    ]
    PIL_GRAYSCALE = 'L'
    PIL_WIDTH_INDEX = 0
    PIL_HEIGHT_INDEX = 1

    def __init__(self, lines):
        self.lines = lines

    def text_to_image(self):
        """Convert text file to a grayscale image.

        arguments:
        textfile_path - the content of this file will be converted to an image
        font_path - path to a font file (for example impact.ttf)
        """

        # choose a font (you can see more detail in the linked library on github)
        font = None
        large_font = 20  # get better resolution with larger size

        for font_filename in self.COMMON_MONO_FONT_FILENAMES:
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
        tallest_line = max(self.lines, key=lambda line: font.getsize(line)[self.PIL_HEIGHT_INDEX])
        max_line_height = font_points_to_pixels(font.getsize(tallest_line)[self.PIL_HEIGHT_INDEX])
        realistic_line_height = max_line_height * 0.8  # apparently it measures a lot of space above visible content
        image_height = int(ceil(realistic_line_height * len(self.lines) + 2 * margin_pixels))

        # width of the background image
        widest_line = max(self.lines, key=lambda s: font.getsize(s)[self.PIL_WIDTH_INDEX])
        max_line_width = font_points_to_pixels(font.getsize(widest_line)[self.PIL_WIDTH_INDEX])
        image_width = int(ceil(max_line_width + (2 * margin_pixels)))

        # draw the background
        background_color = 0  # white
        image = Image.new(self.PIL_GRAYSCALE, (image_width, image_height), color=background_color)
        draw = ImageDraw.Draw(image)

        # draw each line of text
        font_color = 255  # black
        horizontal_position = margin_pixels
        for i, line in enumerate(self.lines):
            vertical_position = int(round(margin_pixels + (i * realistic_line_height)))
            draw.text((horizontal_position, vertical_position), line, fill=font_color, font=font)

        return image