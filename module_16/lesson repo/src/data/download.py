from pathlib import Path

import click
import config
import pandas as pd
from sklearn.datasets import load_digits


@click.command()
@click.argument("output_path", type=Path)
def download(output_path: Path, target: str = config.target):
    data = load_digits()
    x = pd.DataFrame(data.data)
    y = pd.DataFrame({target: data.target})
    df = pd.concat([x, y], axis=1)
    return df.to_csv(output_path, index=False)


if __name__ == "__main__":
    download()
