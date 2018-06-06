from setuptools import setup

requirements = ["graphviz"]

setup(
    name='suffix-trees',
    packages=['suffix_trees'],
    version='0.2.4.4',
    description='Suffix trees, generalized suffix trees and string processing methods',
    author='Peter Us, Nanguage',
    author_email='ptrusr@gmail.com, nanguage@yahoo.com',
    url='https://github.com/nanguage/suffix-trees',
    long_description=open('README.md').read(),
    package_data={},
    include_package_data=True,
    license='MIT',
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
