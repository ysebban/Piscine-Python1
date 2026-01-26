from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    france = data.loc[data["country"] == "France"]
    if france.empty:
        print("France not foud in dataset")
        return
    years_str = [c for c in data.columns if c != "country"]
    years_int = list(map(int, years_str))
    life_plot = france[years_str].iloc[0].astype(float)
    plt.figure()
    plt.plot(years_int, life_plot)
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (years)")
    plt.title("Life Expectancy for France")
    plt.show()


if __name__ == "__main__":
    #try:
        main()
    #except (TypeError, ) as e: