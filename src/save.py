from conf import mongo_conn
import click
import getpass
import bcrypt

conn = mongo_conn()


@click.command()
@click.option('--service', help="Ex: Facebook, Steam, Instagram, etc.")
@click.option('--account', help="Account from service")
@click.option('--password', help="Password from service")
def save(service, account, password):
    if not service:
        print('Please specify a service.')
        return

    master_password = str(getpass.getpass('Your master password...  '))
    if not master_password:
        return

    mongo_person = conn.find_one()

    if not bcrypt.checkpw(master_password.encode('utf-8'), mongo_person['master_password']):
        print('Passwords do not match or do not exists!')
        return

    service_exists = check_if_service_exists_on_mongo(service)
    if service_exists:
        print('Updating service with new data')
        new_accounts = service_exists['accounts']
        account_exists = list(filter(lambda d: d['account'] == account, new_accounts))
        if account_exists:
            for acc in new_accounts:
                if acc['account'] == account:
                    acc['password'] = password
        else:
            new_accounts.append({'account': account, 'password': password})
        query_filter = {'service': str(service).lower()}
        query_set = {'$set': {'accounts': new_accounts}}
        conn.update_one(query_filter, query_set)
        print('Service updated')
    else:
        data = {
            'service': str(service).lower(),
            'accounts': [
                {'account': account, 'password': password}
            ]
        }
        print('Inserting new data')
        conn.insert_one(data)

    print('Success!')


def check_if_service_exists_on_mongo(service):
    query_filter = {'service': str(service).lower()}
    cursor = conn.find_one(query_filter)
    return cursor
