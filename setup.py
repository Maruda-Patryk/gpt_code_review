from setuptools import setup, find_packages

setup(
    name='gpt_code_review',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'openai',
    ],
    entry_points='''
        [console_scripts]
        gpt_code_review=gpt_code_review.main:SomeFunctionClass.cli
    '''
)