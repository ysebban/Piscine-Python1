import sys


def main(av: list[str]) -> int:
    try:
        assert len(av) == 2, "Wrong number of argument"
        try:
            num = int(av[1])
        except ValueError:
            raise AssertionError("Argument must be int")

        if num % 2:
            print("I am uneven")
        else:
            print("I am even")
            return (0)

    except AssertionError as e:
        print(f"AssertionError:{e}")
        return (1)


main(sys.argv)
