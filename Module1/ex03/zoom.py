from load_image import ft_load


def zoom():
    img = ft_load("animal.jpeg")
    x = slice(0, 100)
    img_slice = img[x]
    print(f"New shape after slicing: {img_slice.shape}")
    print(img_slice)