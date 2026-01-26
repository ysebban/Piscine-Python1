import pandas


def load(path: str) -> pandas.DataFrame:
    try:
        data = pandas.read_csv(path)
    except (FileNotFoundError, SystemError) as e:
        print(f"error: {e}")
        return None
    print(f"Loading dataset of dimensions: {data.shape}")
    return data
