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
from pathlib import Path
import os
from functools import partial




def main():
    """
        Apply random padding to an entire dataset of images.
    """
    # Get the command-line arguments
    arguments = parse_command_line_arguments()

    # Assign values from command-line
    source_folder = arguments.source[0]
    destination_folder = arguments.destination[0]

    # Load all images from the directory
    images_found = list(map(str, glob.iglob(source_folder + '/**/*.png', recursive=True)))

    # Get all the target paths
    target_paths = []
    for image in images_found:
        target_paths.append(copy_tree(image, destination_folder)) 

    # Output the images with randomized padding to a new directory.
    list(map(img_transform, images_found, target_paths))

    print('===============IMAGES FOUND===============')
    list(map(print, images_found))
    print('==========================================\n')

    print('============TRANSFORMED IMAGES============')
    list(map(print, target_paths))
    print('==========================================\n')





def copy_tree(source_file, destination_folder):
    """
        Copy a file path while maintaining its subdirectory structure
        and replace its top-level directory with the destination folder.

        Example:
            copy_tree("Downloads/files/example.txt", "Documents") ==> "Documents/files/example.txt"

    Args:
        source_file (string): file path to copy

        destination_folder (string): the new top-level folder

    Returns:
        a new file path with its top-level folder replaced.
    """
    source_path = Path(source_file)
    name_to_change = source_path.parts[0] # Get the first part of the file path
    target_path = "/".join([part if part != name_to_change else destination_folder
                            for part in source_path.parts])[0:]
    return target_path




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
    """
        Apply random padding to an image.

    Args:
        img_in (string): image to add randomized padding to

        img_out (string): destination file path for the new image
    """
     
    margin_min = 50
    margin_max = 400
    background_color = (231, 187, 0) # RGB value: yellowish-gold
    image_size = (1500, 1500)
    
    orig_image = Image.open(img_in)
    rngs = np.random.default_rng()
    padding_margins = rngs.integers(margin_min,margin_max,size=4)
   
    width, height = orig_image.size
    new_width = width + padding_margins[0] + padding_margins[1]
    new_height = height + padding_margins[2] + padding_margins[3]
    
    new_image = Image.new(orig_image.mode, (new_width, new_height), background_color)
    new_image.paste(orig_image, (padding_margins[0],padding_margins[2]))
    resized_imgs = [T.Resize(size=size)(new_image) for size in ([image_size])]

    if img_out is None:
        img_out = f"./img_samples/Trans_{str(uuid.uuid1())[0:8]}.jpg"
    else:
        os.makedirs(os.path.dirname(img_out), exist_ok=True)

    resized_imgs[0].save(img_out)
    #return resized_imgs[0]




if __name__ == '__main__':
    main()
