from snake_config import reports_path, processed_path

rule logistic_regression_forecast:
    input:
        processed_path/"train.csv",
        processed_path/"test.csv"
    output:
        reports_path/"models_forecast"/"logistic_regression.csv"
    shell:
        "python -m src.models.logistic_regression {input} {output}"

rule random_forest_forecast:
    input:
        processed_path/"train.csv",
        processed_path/"test.csv"
    output:
        reports_path/"models_forecast"/"random_forest.csv"
    shell:
        "python -m src.models.random_forest {input} {output}"

rule all_forecast:
    input:
        rules.logistic_regression_forecast.output,
        rules.random_forest_forecast.output