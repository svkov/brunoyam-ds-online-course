from pathlib import Path

import click
import config
import matplotlib.pyplot as plt
import pandas as pd


@click.command()
@click.argument("input_path", type=Path)
@click.argument("output_path", type=Path)
def class_distribution(input_path: Path, output_path: Path, target: str = config.target):
    y = pd.read_csv(input_path)[target]

    plt.hist(y, bins=20)
    plt.xticks(list(range(10)))
    plt.savefig(output_path)


if __name__ == "__main__":
    class_distribution()
