import click

@click.command()
@click.option('-n', '--name', default='world',
              help='Name of the person to greet')
@click.option('-c/-C', '--color/--no-color',
              help='Make the output colorful')
def hello(name, color):
    if color:
        name = click.style(name, fg='yellow')
    click.echo('Hello {}!'.format(name))

if __name__ == '__main__':
    hello()
