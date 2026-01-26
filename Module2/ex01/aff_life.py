from load_csv import load
import matplotlib.pyplot as plt


def main():
    all = load("life_expectancy_years.csv")
    fr = all.loc[all["country"] == "France"]

    xs = fr[]
