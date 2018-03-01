import click, requests, configparser

@click.command()
@click.option('--add', default='',
                help='Add the star')
@click.argument('')

@click.option('--remove',
                help='Remove the star')

@click.option('--show',
                help='Show repositories with/without your star')

#def token_auth(req):
#    config = configparser.ConfigParser()
#    with open('auth.cfg') as f:
#         config.read_file(f)
#    token = config['github']['token']
#    req.headers['Authorization'] = 'token ' + token
#    return req

def new_star(add):
#    session = requests.Session()
#    session.headers = {'User-Agent': 'Ajuska'}
#    session.auth = token_auth
#    add = session.get('https://api.github.com/Ajuska')
#    add = session.put('https://api.github.com/user/starred/pyvec/naucse.python.cz')
#    return add
    click.echo('Star to {} added!' .format(add))

if __name__ == '__main__':
    new_star()
