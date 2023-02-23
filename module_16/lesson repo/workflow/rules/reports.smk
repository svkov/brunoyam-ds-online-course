from snake_config import processed_path, reports_path, raw_path, models

rule calculate_scores:
    input:
        processed_path/"test.csv",
        reports_path/"models_forecast"/"{model}.csv",
    output:
        reports_path/"{model}.csv"
    shell:
        "python -m src.reports.scores {input} {output}"
    

rule draw_class_distribution:
    input:
        raw_path/"digits.csv"
    output:
        reports_path/"class_distribution.png"
    shell:
        "python -m src.reports.class_distribution {input} {output}"

rule all_reports:
    input:
        expand(
            reports_path/"{model}.csv",
            model=models
        ),
        rules.draw_class_distribution.output