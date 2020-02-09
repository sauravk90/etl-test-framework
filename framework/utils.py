import os
import pandas as pd
from dotenv import load_dotenv


def load_env_configs(file_name=".env"):
    env_path = os.getcwd() + '/../{}'.format(file_name)
    load_dotenv(verbose=True, dotenv_path=env_path)

def replace_null(df):
    df.replace({None: pd.np.nan}, inplace=True)

    return df