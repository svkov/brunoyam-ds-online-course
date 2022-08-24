from pathlib import Path

import click
import config
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command()
@click.argument("input_path", type=Path)
@click.argument("output_train_path", type=Path)
@click.argument("output_test_path", type=Path)
def split(
    input_path: Path,
    output_train_path: Path,
    output_test_path: Path,
    features: str = config.features,
    target: list = config.target,
):
    df = pd.read_csv(input_path)
    x_train, x_test, y_train, y_test = train_test_split(
        df[features], df[target], train_size=0.8
    )
    
    train = pd.concat([x_train, y_train], axis=1)
    test = pd.concat([x_test, y_test], axis=1)

    train.to_csv(output_train_path, index=False)
    test.to_csv(output_test_path, index=False)


if __name__ == "__main__":
    split()
