from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


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


def main():
    data = load("population_total.csv")
    if data is None:
        return
    france = data.loc[data["country"] == "France"]
    other = data.loc[data["country"] == "United States"]
    if france.empty or other.empty:
        return
    years_str = [c for c in data.columns
                 if (c != "country" and
                     (int(c) >= 1800 and int(c) <= 2050))]
    years_int = list(map(int, years_str))
    france_pop = parse_pop(france[years_str].iloc[0])
    other_pop = parse_pop(other[years_str].iloc[0])

    plt.figure()
    plt.plot(years_int, france_pop, label="France")
    plt.plot(years_int, other_pop, label="United States")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(EngFormatter(unit=""))
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.legend()
    plt.show()


if __name__ == "__main__":
#try:
    main()
#except (TypeError, ) as e: