from pathlib import Path
from conf import PASS_URL
import json
import click


@click.command()
@click.option('--service', help="Ex: Facebook, Steam, Instagram, etc.")
@click.option('--account', help="Account from service")
@click.option('--password', help="Password from service")
def save(service, account, password):
    print(f'Saving {account} / {password} on {service}')
    # data = {}
    # data_to_save = json.dumps(data, indent=4)
    #
    # with open(PASS_URL, "w") as pass_file:
    #     pass_file.write(data_to_save)


def _validate_file_path():
    expected_file_path = Path(PASS_URL)

    return expected_file_path.is_file()