#!/bin/bash

cd src || exit
python3 ascii_art.py "$@"
{ cd - || exit ; } > /dev/null