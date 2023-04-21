import click
from src import save, retrieve


@click.group(help='CLI tool to manage my passwords')
def cli():
    pass


cli.add_command(save.save)
cli.add_command(retrieve.retrieve, name='get')

if __name__ == "__main__":
    cli()


