=========================
AWS Transcription Grouper
=========================


.. image:: https://img.shields.io/pypi/v/aws_transcription_grouper.svg
        :target: https://pypi.python.org/pypi/aws_transcription_grouper

.. image:: https://img.shields.io/travis/scuerda/aws_transcription_grouper.svg
        :target: https://travis-ci.com/scuerda/aws_transcription_grouper

.. image:: https://readthedocs.org/projects/aws-transcription-grouper/badge/?version=latest
        :target: https://aws-transcription-grouper.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




CLI wrapper for transforming AWS Transcribe JSON files into txt files grouped by speaker.


* Free software: MIT license
* Documentation: https://aws-transcription-grouper.readthedocs.io.


Features
--------

Getting Started
---------------

Install `grouper` from a terminal window with `pip`.

```
pip3 install -U aws-transcription-grouper
```

To run `grouper`, use the following command.

```
grouper AWS_TRANSCRIPTION_FILE.json

```

By default, `grouper` will create a text file in the directory you ran the
command in and will name the text file using the base name of the json file your
provided. For example, the command above would produce a grouped output file
named `AWS_TRANSCRIPTION_FILE.txt`. If you want to specify the output name, you
can do so by using the `-o` or `--output` flag. For example:

```
grouper AWS_TRANSCRIPTION_FILE.json -o important_conversation.txt
```

or 

```
grouper AWS_TRANSCRIPTION_FILE.json -o important_conversation.txt
```

If you do not provide an output file name and the default file name is already
present, grouper will append a number. So running

```
grouper AWS_TRANSCRIPTION_FILE.json
grouper AWS_TRANSCRIPTION_FILE.json
```

will create both `AWS_TRANSCRIPTION.txt` and `AWS_TRANSCRIPTION_1.txt`.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
