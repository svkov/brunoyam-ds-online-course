from pathlib import Path

import click
import config
import pandas as pd
from sklearn.metrics import (accuracy_score, f1_score, precision_score,
                             recall_score)


@click.command()
@click.argument("input_test_path", type=Path)
@click.argument("input_pred_path", type=Path)
@click.argument("output_path", type=Path)
def calculate_accuracy(input_test_path: Path, input_pred_path: Path, output_path: Path, target: str = config.target):
    y_test = pd.read_csv(input_test_path)[target]

    y_pred = pd.read_csv(input_pred_path)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="macro")
    precision = precision_score(y_test, y_pred, average="macro")
    recall = recall_score(y_test, y_pred, average="macro")

    df = pd.DataFrame({
        "accuracy": [accuracy],
        "f1": [f1],
        "precision": [precision],
        "recall": [recall]
    })

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    calculate_accuracy()
