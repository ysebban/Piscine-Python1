import pandas


def load(path: str) -> pandas.DataFrame:
    if not isinstance(path, str):
        return None
    out = pandas.read_csv(path)
    return out
