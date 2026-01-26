from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    Load a jpeg , turn it into numpyArray
    print both shape and array
    slice the array and print new shape
    convert numpy Array back to image
    show the image
    """
    img = ft_load("animal.jpeg")
    print(f"The shape of image is: {img.shape}")
    print(img)
    x = slice(100, 500)
    y = slice(500, 900)
    dim = slice(0, 1)
    slice_img = img[x, y, dim]
    print(f"New shape after slicing: {slice_img.shape}", end=None)
    print(f"or {img[x, y, 0].shape}")
    print(slice_img)
    new_img = slice_img.squeeze(-1)
    plt.imshow(new_img, cmap="gray")
    plt.xlabel("X pixels")
    plt.ylabel("Y pixels")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except (SystemError, TypeError) as e:
        print(f"{type(e).__name__}: {e}")
