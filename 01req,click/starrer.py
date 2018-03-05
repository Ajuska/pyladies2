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

@click.group()
def star():
    pass

@star.command()
@click.argument('url')
def add(url):
    new = session.put('https://api.github.com/user/starred/' + url)
    click.echo('Adding star to {}'.format(url))
    return new


@star.command()
@click.argument('url')
def remove(url):
    remove = session.delete('https://api.github.com/user/starred/' + url)
    click.echo('Removing star from {}'.format(url))
    return remove

@star.command()
@click.argument('urls', nargs=-1, required=True)
def show(urls):
    for url in urls:
        link = session.get('https://api.github.com/user/starred/' + url)
        if link.status_code == 204:
            click.echo('* {}'.format(url))
        else:
            click.echo('  {}'.format(url))

if __name__ == '__main__':
    star()
