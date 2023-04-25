from conf import mongo_conn
import click
import bcrypt

conn = mongo_conn()


@click.command()
@click.option('--password', help="Master password")
def create_person(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    person_dict = {
        'master_password': hashed_password,
        'services': []
    }
    save(person_dict)


def save(person):
    print('Creating person data.')
    conn.insert_one(person)
    print('Person data has been created!')
