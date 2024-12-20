import functools
import os

from dotenv import load_dotenv, set_key

from src.constants import DOTENV_PATH, ENV_VAR_NAMES


def verify_dotenv(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not os.path.isfile(DOTENV_PATH):
            generate_dotenv()
        return func(*args, **kwargs)
    return wrapper


def generate_dotenv():
    with open(DOTENV_PATH, 'w') as f:
        for env_var_name in ENV_VAR_NAMES:
            f.write(f"{env_var_name}=''\n")


@verify_dotenv
def load_env_vars():
    load_dotenv()


@verify_dotenv
def update_env_vars(**kwargs):
    for var_name, var_val in kwargs.items():
        os.environ[var_name] = var_val
        set_key(DOTENV_PATH, var_name, os.environ[var_name])
