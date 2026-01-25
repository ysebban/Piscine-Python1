import pandas


def load(path: str) -> pandas.DataFrame:
    try:
        data = pandas.read_csv(path)
    except (FileNotFoundError, SystemError) as e:
        print(f"error: {e}")
        return None
    print(f"Loading dataset of dimensions: {data.shape}")
    return data


def parse_pop(data_pop: list[str]) -> list[float]:
    parsed = []
    for entry in data_pop:
        if entry.endswith(("k", "K")):
            parsed.append(float(entry[: -1]) * 1_000)
        elif entry.endswith(("m", "M")):
            parsed.append(float(entry[: -1]) * 1_000_000)
        else:
            parsed.append(float(entry))
    return parsed