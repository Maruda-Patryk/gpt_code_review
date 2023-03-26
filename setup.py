from setuptools import setup

setup(
    name='gtp_code_review',
    version='0.1',
    description='A description of my package',
    author='Patryk Maruda',
    author_email='patrykmaruda@gmail.com',
    url='https://github.com/yourusername/my_package',
    packages=['gtp_code_review'],
    install_requires=[
        'click',
        'GitPython',
    ],
)
