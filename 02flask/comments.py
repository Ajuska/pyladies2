import requests, configparser

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


response = session.post(
    'https://api.github.com/repos/Ajuska/test_repository/issues/2/reactions',
    headers={'Accept': 'application/vnd.github.squirrel-girl-preview+json'},
    json={'content': '+1'}
)

response.raise_for_status()
