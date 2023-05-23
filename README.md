# ASCII Art Generator
A customisable script to transform images into ASCII art.

<hr>

![CODEQL](https://github.com/hwixley/ascii-art-generator/actions/workflows/codeql.yml/badge.svg) ![Python](https://img.shields.io/badge/Python-3.8.10-purple?labelColor=gray&style=flat) ![Version](https://img.shields.io/badge/Version-0.0.1-blue?labelColor=gray&style=flat)

<hr>

Input image                |  Output ASCII
:-------------------------:|:-------------------------:
![cage](https://github.com/hwixley/ascii-art-generator/assets/57837950/2380ff4d-09a9-433e-a4e4-a0ff00c451fe) | <img src="https://github.com/hwixley/ascii-art-generator/assets/57837950/3800d64b-2842-4ff7-841c-a5f02ff51215" style="width: 1200px">


## Installation

1. Clone the repository:
   ```
   git clone git@github.com:hwixley/ascii-art-generator.git
   ```
2. Install the dependencies:
   ```
   pip3 install -r requirements.txt
   ```

## Run the script
You can run the script using shell:
```
chmod +x ascii-art-generator.sh && ./ascii-art-generator.sh
```
Or using python:
```
python3 src/ascii_art.py
```

## Arguments
All the following arguments are optional.

- __Image:__ the path of your input image, defaults to Nick Cage.<br>`-i <img_path>` &nbsp; or &nbsp;  `--img <img_path>`

- __Image Width:__ the "ASCII pixel" (two horizontally adjacent ASCII characters) width of your output ASCII image, defaults to `80`.<br>`-w <img-width>` &nbsp; or &nbsp; `--img-width <img-width>`

- __Charset:__ the size of charset for your ASCII image (options: `tiny`, `small`, `medium`, `large`), defaults to `small`.<br>`-c <charset>` &nbsp; or &nbsp; `--charset <charset>`

- __Sampler:__ the pixel density sampler type (options: `linear`, `log`, `exp`), defaults to `linear`.<br>`-s <sampler>` &nbsp; or &nbsp; `--sampler <sampler>`

- __Lower Bound:__ the lower bound of pixel density sampling, defaults to `0.2`. Bounded in the range [0,1].<br>`-l <lower-ptg>` &nbsp; or &nbsp; `--lower-ptg <lower-ptg>`

- __Upper Bound:__ the upper bound of pixel density sampling, defaults to `0.4`. Bounded in the range [0,1].<br>`-u <upper-ptg>` &nbsp; or &nbsp; `--upper-ptg <upper-ptg>`

- __Save/generate image:__ if specified will put the ASCII art into a PNG.<br>`-g` &nbsp; or &nbsp; `--gen-img`

### Utility Args

- __Help:__ lists available arguments.<br>`-h` &nbsp; or &nbsp; `--help`

- __Version:__ lists current version.<br> `-v` &nbsp; or &nbsp; `--version`
