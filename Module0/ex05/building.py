import sys


def count_string(text: str):
    """
    takes a string for arguments and display all counted characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0,
        "all": 0
    }
    for c in text:
        count["all"] += 1
        if c.isupper():
            count["upper letters"] += 1
        elif c.islower():
            count["lower letters"] += 1
        elif c.isdigit():
            count["digits"] += 1
        elif c.isspace():
            count["spaces"] += 1
        else:
            count["punctuation marks"] += 1

    print(f"The text contains {count['all']} characters")
    for key, value in count.items():
        if key != "all":
            print(f"{value} {key}")


def prompt_client():
    """
    Prompt user for some text and call count_string
    """
    print("What is the text to count?")
    text = sys.stdin.readline()
    count_string(text)


def main(av: list[str]) -> int:
    """
    Program entry point
    run test and handles all errors
    """
    try:
        assert len(av) <= 2, "Assertion: Wrong number of argument"
        if len(av) == 1:
            prompt_client()
        else:
            count_string(av[1])
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    main(sys.argv)
