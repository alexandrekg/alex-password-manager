import click

@click.command()
@click.option('--service_name', help='Save password from ... (Ex: Facebook, Instagram, Github, etc.)')
@click.option('--add', help='')
@click.option('--pass', help='Your passwor')
def run():
    print('Run!')


if __name__ == "__main__":
    run()