import matplotlib.pyplot as plt
import numpy as np
import uuid
import torch
import torchvision.transforms as T
from PIL import Image
from pathlib import Path
import argparse
import sys
import glob



def main():
    # Get the command-line arguments
    arguments = parse_command_line_arguments()

    # Assign values from command-line
    source_folder = arguments.source[0]
    destination_folder = arguments.destination[0]

    # Load all images from the directory
    images = map(str, glob.iglob(source_folder + '/**/*.png', recursive=True))
    #images = []

    #for image in glob.iglob(source_folder + '/**/*.png', recursive=True):
    #    images.append(image)
    #    print(image)

    print(list(images))




def parse_command_line_arguments():
    """ 
        Parse the arguments from the command-line.
        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        the parser with command-line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--source', nargs=1, required=True,
                        help='Source folder containing images.')

    parser.add_argument('-d', '--destination', nargs=1, required=True,
                        help='Destination folder to save randomized images to.')

    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()




def img_transform(img_in, img_out=None):
     
    margin_min = 50
    margin_max = 400
    background_color = (231, 187, 0) # RGB value: yellowish-gold
    
    orig_image = Image.open(img_in)
    rngs = np.random.default_rng()
    padding_margins = rngs.integers(margin_min,margin_max,size=4)
   
    width, height = orig_image.size
    new_width = width + padding_margins[0] + padding_margins[1]
    new_height = height + padding_margins[2] + padding_margins[3]
    
    new_image = Image.new(orig_image.mode, (new_width, new_height), background_color)
    new_image.paste(orig_image, (padding_margins[0],padding_margins[2]))
    resized_imgs = [T.Resize(size=size)(new_image) for size in ([(1500,1500)])]

    if img_out is None:
        img_out = f"./img_samples/Trans_{str(uuid.uuid1())[0:8]}.jpg"
    resized_imgs[0].save(img_out)
    return resized_imgs[0]




if __name__ == '__main__':
    main()
