from distutils.core import setup

setup(
    name='OAuth2',
    version='0.0.1',
    author='GraphEffect, Inc.',
    author_email='nate@grapheffect.com',
    packages=['oauth2', 'oauth2.test'],
    scripts=[],
    url='https://github.com/GraphEffect/oauth2',
    license='LICENSE.txt',
    description='OAuth 2.0 compliant client and server library.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 0.14",
        "PyCrypto >= 2.6"
    ]
)
