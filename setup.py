"""
Setup module
"""

import setuptools

with open(file='README.md', mode='r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='kex',
    version='0.0.1',
    description='Kivy extension library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.9',
    install_requires=[
        'numpy==1.22.3',
        'kivy==2.1.0',
    ],
    packages=setuptools.find_packages(
        include=['kex']
    ),
)
