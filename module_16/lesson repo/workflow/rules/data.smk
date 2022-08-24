from snake_config import raw_path, interim_path, processed_path

rule download_data:
    output: 
        raw_path/"digits.csv"
    shell:
        "python -m src.data.download {output}"

rule preprocessing_data:
    input:
        raw_path/"digits.csv"
    output:
        interim_path/"scaled_digits.csv"
    shell:
        "python -m src.data.preprocessing {input} {output}"

rule train_test_split:
    input:
        interim_path/"scaled_digits.csv"
    output:
        processed_path/"train.csv",
        processed_path/"test.csv"
    shell:
        "python -m src.data.train_test_split {input} {output}"

rule all_data:
    input:
        rules.download_data.output,
        rules.preprocessing_data.output,
        rules.train_test_split.output
