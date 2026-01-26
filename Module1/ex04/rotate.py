from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def legit_transpose(img):
    """
    Takes an img and transpose it(change x and y axis)
    """
    H, W, C = img.shape
    out = np.empty((W, H, C), dtype=img.dtype)
    for y in range(H):
        for x in range(W):
            out[x, y, :] = img[y, x, :]
    return out


def main():
    """
    Load a wonderfull racoon , zoom it and rotate it
    Print a lot of meaningfull data in the way
    """
    img = ft_load("animal.jpeg")
    x = slice(100, 500)
    y = slice(500, 900)
    dim = slice(0, 1)
    slice_img = img[x, y, dim]
    print(f"The shape of image is: {slice_img.shape}", end=None)
    print(f"or {img[x, y, 0].shape}")
    print(slice_img)

    rot90_img = legit_transpose(slice_img)
    print(f"New shape after Transpose: {rot90_img.shape}")
    print(rot90_img)
    plt.imshow(rot90_img, cmap="gray")
    plt.xlabel("X pixels")
    plt.ylabel("Y pixels")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except (SystemError, TypeError, OverflowError, KeyboardInterrupt, FileNotFoundError) as e:
        print(f"{type(e).__name__}: {e}")
