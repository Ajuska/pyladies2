import requests, click, configparser

session = requests.Session()
session.headers = {'User-Agent': 'Python'}

def token_auth(req):
    config = configparser.ConfigParser()
    with open('auth.cfg') as f:
         config.read_file(f)
    tk = config['github']['token']
    req.headers['Authorization'] = 'token ' + tk
    return req

session.auth = token_auth
r = session.get('https://api.github.com/user')

@click.group()
def star():
    pass

@star.command()
@click.argument('url')
def new_star(url):
    add = session.put('https://api.github.com/user/starred/' + url)
    click.echo('Adding star to {}'.format(url))
    return add


@star.command()
@click.argument('url')
def remove_star(url):
    remove = session.delete('https://api.github.com/user/starred/' + url)
    click.echo('Removing star from {}'.format(url))
    return remove

@star.command()
@click.argument('url')
def show_stars(url):
    link = session.get('https://api.github.com/user/starred/' + url)
    if link.status_code == 204:
        click.echo('Star is at {}'.format(url))
        print('* ' + url)
    else:
        click.echo('Star is not at {}'.format(url))
        print('  ' + url)

# @click.command()
# @click.option('--add', default='url',
#                 help='Add the star')
# @click.argument('')
#
# @click.option('--remove',
#                 help='Remove the star')
#
# @click.option('--show',
#                 help='Show repositories with/without your star')


if __name__ == '__main__':
    #remove_star()
    show_stars()
