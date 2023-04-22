import click
from conf import mongo_conn
import subprocess


@click.command()
@click.option('--service', default="", help="If you want to get a specific data")
@click.option('--account', default="", help="Specify account you want to get password")
def retrieve(service, account):
    if not service:
        print('Please specify a service.')
        return

    print('Retrieving data...')
    data = get_data_from_mango(service)
    print('Data retrieved')
    if data:
        if len(data) == 1:
            return copy_pass(data[service][0]['password'])

        if len(data) > 1 and not account:
            print('Please specify an account to get password')
            return

        return copy_pass(data[service])


def get_data_from_mango(service):
    filter = {}

    if service:
        filter = {service: {'$exists': True}}

    data = mongo_conn().find_one(filter, {'_id': 0})
    return data


def copy_pass(password):
    password_cmd = f'echo {password.strip()}|clip'
    print('Password copied')
    return subprocess.check_call(password_cmd, shell=True)
