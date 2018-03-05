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

@click.command()
@click.option('--add', 'url',
                help='Add the star')
#@click.option('--remove', 'url2',
#                 help='Remove the star')

# @click.option('--show',
#                 help='Show repositories with/without your star')

def new_star(url):
    add = session.put('https://api.github.com/user/starred/' + url)
    click.echo('Adding star to {}'.format(url))
    return add

if __name__ == '__main__':
    new_star()
