from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='FreeDay',
    version='0.0.1',
    description='Basic tool to download free day',
    Long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Kacper Padykuła',
    author_email='kakip1997@gmail.com',
    license='MIT',
    classifiers='classifiers',
    keywords='freeday',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'requests',
        'unittest'
    ]
)