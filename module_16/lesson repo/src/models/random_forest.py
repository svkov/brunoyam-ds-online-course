from pathlib import Path

import click
import config
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


@click.command()
@click.argument("input_train_path", type=Path)
@click.argument("input_test_path", type=Path)
@click.argument("output_path", type=Path)
def linear_regression(
    input_train_path: Path,
    input_test_path: Path,
    output_path: Path,
    features: list = config.features,
    target: str = config.target,
):
    train = pd.read_csv(input_train_path)
    test = pd.read_csv(input_test_path)

    x_train, y_train = train[features], train[target]
    x_test = test[features]

    model = RandomForestClassifier(max_depth=15, n_estimators=200)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    pd.DataFrame({"target": y_pred}).to_csv(output_path, index=False)


if __name__ == "__main__":
    linear_regression()
