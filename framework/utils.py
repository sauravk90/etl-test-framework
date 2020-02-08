import os
from dotenv import load_dotenv


def load_env_configs(file_name=".env"):
    #print("loading contents of .env")
    env_path = os.getcwd() + '/../{}'.format(file_name)
    load_dotenv(verbose=True, dotenv_path=env_path)