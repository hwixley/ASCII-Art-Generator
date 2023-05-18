# ASCII Art Generator

A simple script to transform images into ASCII art.

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

- __Image:__ the path of your input image, defaults to Nick Cage.
`-i <img_path>` or `--img <img_path>`
<br>
- __Charset:__ the size of charset for your ASCII art (options: `tiny`, `small`, `medium`, `large`), defaults to `medium`.
`-c <charset>` or `--charset <charset>`
<br>
- __Sampler:__ the pixel density sampler type (options: `linear`, `log`, `exp`), defaults to `linear`.
`-s <sampler>` or `--sampler <sampler>`
<br>
- __Lower Bound:__ the lower bound of pixel density sampling, defaults to 0.1. Bounded in the range [0,1].
  `-l <lower-ptg>` or `--lower-ptg <lower-ptg>`
<br>
- __Upper Bound:__ the upper bound of pixel density sampling, defaults to 0.5. Bounded in the range [0,1].
`-u <upper-ptg>` or `--upper-ptg <upper-ptg>`
<br>