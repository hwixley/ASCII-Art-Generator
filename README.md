# ASCII Art Generator
A customisable script to transform images into ASCII art.

<hr>

![CODEQL](https://github.com/hwixley/ascii-art-generator/actions/workflows/codeql.yml/badge.svg)

<hr>

Input image                |  Output ASCII
:-------------------------:|:-------------------------:
![cage](https://github.com/hwixley/ascii-art-generator/assets/57837950/2380ff4d-09a9-433e-a4e4-a0ff00c451fe) | ![cage-ascii2](https://github.com/hwixley/ascii-art-generator/assets/57837950/d2e3cfa9-7c9c-40cc-8eb2-e575ffe7eafe)

## Installation

1. Clone the repository:
   ```
   git clone git@github.com:hwixley/ascii-art-generator.git
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Make the script executable (if you want to use Shell):
   ```
   chmod +x ascii-art-generator.sh
   ```

## Run the script
You can run the script using shell:
```
./ascii-art-generator.sh <args?>
```
Or using python:
```
python src/AsciiArt.py <args?>
```

## Arguments
All the following arguments are optional.

- __Image:__ the path of your input image, defaults to Nick Cage.<br>`-i <img_path>` or `--img <img_path>`

- __Charset:__ the size of charset for your ASCII art (options: `tiny`, `small`, `medium`, `large`), defaults to `small`.<br>`-c <charset>` or `--charset <charset>`

- __Sampler:__ the pixel density sampler type (options: `linear`, `log`, `exp`), defaults to `linear`.<br>`-s <sampler>` or `--sampler <sampler>`

- __Lower Bound:__ the lower bound of pixel density sampling, defaults to `0.2`. Bounded in the range [0,1].<br>`-l <lower-ptg>` or `--lower-ptg <lower-ptg>`

- __Upper Bound:__ the upper bound of pixel density sampling, defaults to `0.4`. Bounded in the range [0,1].<br>`-u <upper-ptg>` or `--upper-ptg <upper-ptg>`
