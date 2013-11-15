from distutils.core import setup

setup(
    name='oauth2lib',
    version='1.0.0',
    author='Nate Ferrero',
    author_email='nateferrero@gmail.com',
    packages=['oauth2lib', 'oauth2lib.tests'],
    scripts=[],
    url='https://github.com/NateFerrero/oauth2lib',
    license='LICENSE.md',
    description='OAuth 2.0 compliant client and server library.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 0.14"
    ]
)
