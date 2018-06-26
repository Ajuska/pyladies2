from setuptools import setup, find_packages

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
    packages=find_packages(),
    classifiers=[
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'pyglet',
        'flask',
        'click>=6',
    ],
    zip_safe=False,
)

#instalace setup --- python setup.py install
#verze ve venv ---- python -m pip freeze
#tvorba balicku --- python setup.py sdist
#instalace/upgrade balicku -- python -m pip install --upgrade dist/ajuska-demo-2018-0.1.0.tar.gz
