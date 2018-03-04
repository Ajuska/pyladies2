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



def new_star(url):
    add = session.put('https://api.github.com/user/starred/' + url)
    return add

def remove_star(url):
    remove = session.delete('https://api.github.com/user/starred/' + url)
    return remove

def show_stars(url):
    link = session.get('https://api.github.com/user/starred/' + url)
    if link.status_code == 204:
        print('* ' + url)
    else:
        print('  ' + url)

ondra = show_stars('OndrejVicar/LunchMenuChecker')
pyvec = show_stars('pyvec/naucse.python.cz')
web = show_stars('Ajuska/web')
