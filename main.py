import click
from pathlib import Path

from conf import PASS_URL


@click.option('--service_name',  help='Save password from ... (Ex: Facebook, Instagram, Github, etc.)')
@click.option('--account', help='Your username, account, e-mail, etc...')
@click.option('--password', help='Your password')
def run(service_name, account, password):
    print(f'Your {service_name} data: {account} / {password}')


@click.command()
@click.option('--action')
def cli(action):
    if action == 'get':
        get_data()
    elif action == 'save':
        save_data()


def get_data():
    return _validate_file_path()


def _validate_file_path():
    expected_file_path = Path(PASS_URL)

    return expected_file_path.is_file()


def save_data():
    pass


if __name__ == "__main__":
    cli()