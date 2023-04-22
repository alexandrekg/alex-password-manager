from conf import mongo_conn
import click


@click.command()
@click.option('--service', help="Ex: Facebook, Steam, Instagram, etc.")
@click.option('--account', help="Account from service")
@click.option('--password', help="Password from service")
def save(service, account, password):
    conn = mongo_conn()
    data = {
        service: [
            {'account': account, 'password': password}
        ]
    }
    print('Inserting new data')
    conn.insert_one(data)
    print('Success!')
