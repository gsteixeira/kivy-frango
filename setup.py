import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='kivy-frango',
    version='0.0.3',
    packages=find_packages(),
    include_package_data=True,
    license='GNU License',  # example license
    description='Framework like Django for Kivy',
    long_description=README,
    url='https://www.gstsistemas.com/',
    author='Gustavo Selbach Teixeira',
    author_email='gsteixei@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Mobile App',
        'Framework :: Kivy',
    ],
    install_requires=[
          'peewee',
          'Kivy',
      ],
    package_data={
            #'frango': ['frango/*', ]
        },
    
    scripts=['frango/bin/frango-admin'],
)
