import click, requests, configparser

@click.command()
@click.argument('directory')
def cd(directory):
    """Change the current directory"""
    click.echo('Changing to directory {}'.format(directory))

@click.command()
@click.argument('source', nargs=-1)
@click.argument('destination', nargs=1)
def mv(source, destination):
    """Move any number of files to one destination"""
    for filename in source:
        click.echo('Moving {} to {}'.format(filename, destination))
