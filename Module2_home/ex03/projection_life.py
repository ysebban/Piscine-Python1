from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    data_life = load("life_expectancy_years.csv")
    data_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if data_life is None or data_gdp is None:
        return
    year = "1900"

    gdp_1900 = data_gdp[["country", year]].rename(columns={year: "gdp_per_person"})
    life_1900 = data_life[["country", year]].rename(columns={year: "life_expectancy"})
    
    merged = pd.merge(gdp_1900, life_1900, on="country", how="inner")
    merged["gdp_per_person"] = pd.to_numeric(merged["gdp_per_person"], errors="coerce")
    merged["life_expectancy"] = pd.to_numeric(merged["life_expectancy"], errors="coerce")
    merged = merged.dropna(subset=["gdp_per_person", "life_expectancy"])

    plt.figure()
    plt.scatter(
        merged["gdp_per_person"],
        merged["life_expectancy"],
        label=f"Countries ({year})",
        s=20,
        alpha=0.7,
    )
    plt.title(f"Life expectancy vs GDP per person ({year})")
    plt.xlabel("GDP per person (PPP, inflation-adjusted)")
    plt.ylabel("Life expectancy (years)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()