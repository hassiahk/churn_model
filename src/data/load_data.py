import yaml
import argparse
import pandas as pd

def read_params(config_path):
    """
    read parameters from params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """

    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def load_data(data_path, selected_features):
    """
    load data from given path
    input: csv path, required features
    output: pandas dataframe with only selected features from config file
    """
    df = pd.read_csv(data_path, sep=',', encoding='utf-8')
    return df.loc[selected_features]


def load_raw_data(config_path):
    """
    load data from (data/external) to (data/raw)
    input: config_path
    output: saves the file to data/raw folder
    """
    # load the params file
    config = read_params(config_path)

    # read the necessary paths
    external_data_path = config['external_data_config']['external_data_csv']
    raw_data_path = config['raw_data_config']['raw_data_csv']

    selected_features = config['raw_data_config']['model_var']

    # write data to raw folder
    df = load_data(external_data_path, selected_features)
    df.to_csv(raw_data_path, index=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')

    parsed_args = args.parse_args()
    load_raw_data(config_path=parsed_args.config)
