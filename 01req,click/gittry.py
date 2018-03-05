import click, requests, configparser

@click.group()
def git2():
    pass

@git2.command()
def commit():
    message = click.edit('Made some changes')
    click.echo('Making commit with message: {}'.format(message))

@git2.command()
@click.argument('files', nargs=-1)
def add(files):
    for file in files:
        click.echo('Adding {}'.format(file))

git2()
