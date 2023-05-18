#!/bin/bash

cd src || exit
python3 AsciiArt.py "$@"
cd - || exit