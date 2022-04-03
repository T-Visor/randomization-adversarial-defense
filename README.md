# Ricochet Pre-Processing
Applies randomized padding to images containing faces, serving as a data augmentation
technique to train robust facial recognition systems.

## Test Environment
- Python 3.10
- Arch Linux

## Setup
Install Python dependencies with the following command:
``` sh
$ pip3 install -r requirements.txt
``` 

## Usage

``` sh
$ randomization.py [-h] -s SOURCE -d DESTINATION

options:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source folder containing images.
  -d DESTINATION, --destination DESTINATION
                        Destination folder to save randomized images to.
```

