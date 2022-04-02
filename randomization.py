from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

import torch
import torchvision.transforms as T


def img_transform(img_in, img_out=None):
    from PIL import Image
    import torchvision.transforms as T
    import numpy as np
    import uuid
     
    margin_min = 50
    margin_max = 400
    background = (0, 0, 64)
    
    orig_image = Image.open(img_in)
    rngs = np.random.default_rng()
    padding_margins = rngs.integers(margin_min,margin_max,size=4)
   
    width, height = orig_image.size
    new_width = width + padding_margins[0] + padding_margins[1]
    new_height = height + padding_margins[2] + padding_margins[3]
    
    new_image = Image.new(orig_image.mode, (new_width, new_height), background)
    new_image.paste(orig_image, (padding_margins[0],padding_margins[2]))
    resized_imgs = [T.Resize(size=size)(new_image) for size in ([(150,150)])]

    if img_out is None:
        img_out = f"./img_samples/Trans_{str(uuid.uuid1())[0:8]}.jpg"
    resized_imgs[0].save(img_out)
    return resized_imgs[0]
