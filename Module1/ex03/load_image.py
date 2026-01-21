import numpy as np
from PIL import Image


def ft_load(path: str):
    if not isinstance(path, str):
        return ("Path isn't a string")
    image = Image.open(path)
    np_image = np.asarray(image)
    print(f"Shape of loaded image is: {np_image.shape}")
    return np_image