import pandas as pd
import yaml


def process_data(frac=0.1, split="train"):
    df = pd.read_csv("data/raw/{}.csv".format(split))
    df.columns = ["Unnamed: 0", "input_text", "output_text"]
    df_new = df.sample(frac=frac, replace=True, random_state=1)
    df_new.to_csv("data/processed/{}.csv".format(split))


if __name__ == "__main__":
    with open("data_params.yml") as f:
        params = yaml.safe_load(f)

    process_data(frac=params["split"], split="train")
    process_data(frac=params["split"], split="test")
    process_data(frac=params["split"], split="validation")
