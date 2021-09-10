#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['tscribe', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Sasha Cuerda",
    author_email='sasha.cuerda@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI wrapper for transforming AWS Transcribe JSON files into txt files grouped by speaker.",
    entry_points={
        'console_scripts': [
            'grouper=aws_transcription_grouper.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='aws_transcription_grouper',
    name='aws_transcription_grouper',
    packages=find_packages(include=['aws_transcription_grouper', 'aws_transcription_grouper.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/scuerda/aws_transcription_grouper',
    version='0.1.1',
    zip_safe=False,
)
