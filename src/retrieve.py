import click
from pathlib import Path
from conf import PASS_URL


@click.command()
@click.option('--service', default="", help="If you want to get a specific data")
def retrieve(service):
    if service:
        print('Get specified data')
    else:
        data = _get_json_data()
        print(data)


def _get_json_data():
    retrieved_data = []
    if not _validate_file_path():
        print("Can't acess requested data.")
        return

    with open(PASS_URL, "r") as data:
        for d in data:
            retrieved_data.append(d)

    return retrieved_data

def _validate_file_path():
    expected_file_path = Path(PASS_URL)

    return expected_file_path.is_file()