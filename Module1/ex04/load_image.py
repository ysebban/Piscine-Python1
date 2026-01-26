import numpy as np
from PIL import Image


def ft_load(path: str):
    """
    Load an image according to path, must be string
    Convert it to numpy array
    Print the shape of the image
    Returns a print in case of errors
    Returns a numpy Array of the image
    """
    if not isinstance(path, str):
        return ("Path isn't a string")
    image = Image.open(path)
    np_image = np.asarray(image)
    print(f"Shape of loaded image is: {np_image.shape}")
    return np_image
