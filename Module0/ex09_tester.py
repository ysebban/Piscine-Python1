import ft_package
from ft_package import count_string


def has_doc(obj):
    return obj.__doc__ is not None


def main():
    exported = [
        getattr(ft_package, name)
        for name in ft_package.__all__
        if hasattr(ft_package, name)
    ]

    documented = ft_package.ft_filter(has_doc, exported)

    for obj in documented:
        print(f"{obj.__name__}:")
        print(obj.__doc__.strip(), end="\n\n")
        count_string(obj.__doc__.strip())

    return 0


if __name__ == "__main__":
    main()
