from ft_filter import ft_filter
import sys


def main(av: list[str]) -> int:
    """
    Filters a string based on numbers of char and print result
    """
    try:
        assert len(av) == 3, "the arguments are bad"
        text = av[1]
        num = int(av[2])

        words = [W for W in text.split(" ") if W]
        result = ft_filter(lambda w: len(w) > num, words)

        print(result)
        return 0

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return 1


if __name__ == "__main__":
    main(sys.argv)
