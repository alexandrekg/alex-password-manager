import click
import getpass
from conf import mongo_conn
import subprocess
import bcrypt

conn = mongo_conn()

@click.command()
@click.option('--service', default="", help="If you want to get a specific data")
@click.option('--account', default="", help="Specify account you want to get password")
def retrieve(service, account):
    if not service:
        print('Please specify a service.')
        return

    master_password = str(getpass.getpass('Your master password...  '))
    if not master_password:
        return

    mongo_person = conn.find_one()

    if not bcrypt.checkpw(master_password.encode('utf-8'), mongo_person['master_password']):
        print('Passwords do not match!')
        return

    print('Retrieving data...')
    data = get_data_from_mango(service)
    if data:
        format_service_str = str(service).lower()
        print('Data retrieved')
        if len(data) == 1:
            return copy_pass(data['accounts'][0]['password'])

        if len(data) > 1 and not account:
            print('Please specify an account to get password')
            return

        return copy_pass(data[format_service_str])
    else:
        print('Data has not been found for this service.')


def get_data_from_mango(service):
    if not service:
        print('Please, specify a service name to copy password')
        return

    filter_query = {'service': str(service).lower()}
    return mongo_conn().find_one(filter_query, {'_id': 0})


def copy_pass(password):
    password_cmd = f'echo {password.strip()}|clip'
    print('Password copied')
    return subprocess.check_call(password_cmd, shell=True)
