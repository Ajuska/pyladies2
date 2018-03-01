import click, requests, configparser

@click.group()
def starrer():
    pass

@starrer.command()
@click.option('--add', default='',
                help='Add the star')
@click.argument('add_star')
def add(add_star):
    click.echo('Hello {}'.format(add_star))

@starrer.command()
@click.argument('url')
def remove(url):
    click.echo('Godbye {}'.format(url))

if __name__ == '__main__':
    add()
