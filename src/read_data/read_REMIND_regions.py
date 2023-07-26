import os
from src.tools.config import cfg
import pandas as pd


def get_REMIND_regions():
    remind_data_path = os.path.join(cfg.data_path, 'original', 'remind', 'REMINDRegions.csv')
    df = pd.read_csv(remind_data_path)
    df.set_index('country', inplace=True)
    return df


if __name__ == '__main__':
    df = get_REMIND_regions()
    print(df)
