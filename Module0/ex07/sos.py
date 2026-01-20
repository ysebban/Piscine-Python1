import sys


def main(av: list[str]):
    """
    Translate input in morse
    catches errors
    """

    MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    try:
        assert len(av) == 2, "Wrong numbers of arguments"
        result = []
        for c in av[1]:
            key = c.upper()
            if key in MORSE:
                result.append(MORSE[key])
            else:
                raise AssertionError(f"Character not supported : {c}")
        print(" ".join(result))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(sys.argv)
