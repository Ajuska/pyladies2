from setuptools import setup

with open('README.md') as file:
    readme = file.read()

setup(
    name='ajuska-demo-2018',
    version='0.1.0',
    description='Prints "hello" in Czech',
    author='Andrea Kopecna',
    author_email='a.kopecna1@gmail.com',
    license='CC-0',
    # url='http://' --> domain of the project
    long_description=readme,
    py_modules=['demo'],
    classifiers=[
        'License :: CC0 1.0 Universal (CC0 1.0)',
        'Programming Language :: Python :: 3.5',
    ]
    zip_safe=False,
)

#instalace setup --- python setup.py install
#verze ve venv ---- python -m pip freeze
#tvorba balicku --- python setup.py sdist
#instalace/upgrade balicku -- python -m pip install --upgrade dist/ajuska-demo-2018-0.1.0.tar.gz
