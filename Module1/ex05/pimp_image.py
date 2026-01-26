import numpy as np
import PIL as Image


def ft_invert(array: np.array) -> np.array:
    """filters an image by inverting colors """
    out = array.copy()
    out = 255 - out
    print(f"The shape of image is {out.shape}")
    print(out)
    print("Inverted colors")
    Image.Image.fromarray(out).show()
    return out


def ft_red(array: np.array) -> np.array:
    """ filters an image on RED scale only """
    out = array.copy()
    out[:, :, 1] = 0
    out[:, :, 2] = 0
    print(f"The shape of image is {out.shape}")
    print(out)
    print("Red color only kept")
    Image.Image.fromarray(out).show()
    return out


def ft_green(array: np.array) -> np.array:
    """ filters an image on GREEN scale only"""
    out = array.copy()
    out[:, :, 0] = 0
    out[:, :, 2] = 0
    print(f"The shape of image is {out.shape}")
    print(out)
    print("Green color only kept")
    Image.Image.fromarray(out).show()
    return out


def ft_blue(array: np.array) -> np.array:
    """filters an image on BLUE scale only"""
    out = array.copy()
    out[:, :, 0] = 0
    out[:, :, 1] = 0
    print(f"The shape of image is {out.shape}")
    print(out)
    print("Blue color only kept")
    Image.Image.fromarray(out).show()
    return out


def ft_grey(array: np.array) -> np.array:
    """Filters image on a grey scale"""
    tmp = array.copy()
    out = (0.299 * tmp[:, :, 0] + 0.587 * tmp[:, :, 1] + 0.114 * tmp[:, :, 2])
    print(f"The shape of image is {out.shape}")
    print(out)
    print("All colors on a gray scale")
    Image.Image.fromarray(out).show()
    return out
