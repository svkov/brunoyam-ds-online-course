from pathlib import Path

import click
import config
import pandas as pd


@click.command()
@click.argument("input_path", type=Path)
@click.argument("output_path", type=Path)
def process_data(input_path: Path, output_path: Path, features: list = config.features):
    df = pd.read_csv(input_path)
    mean = df[features].values.mean()
    std = df[features].values.std()
    df[features] = (df[features] - mean) / std
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    process_data()
