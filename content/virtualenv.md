Title: virtualenv
Date: 2015-11-06
Category: Notes
Tags: code, pelican, python
Slug: virtualenv
Authors: Amit
Summary: Quick guide on use of virtualenv

A [Virtual Environment] [ve] is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them.

[ve]: http://docs.python-guide.org/en/latest/dev/virtualenvs/ "Hitchhiker's Guide to Python"

Installing virtualenv:
    
    :::bash
    pip install virtualenv

Create a virtual environment to install into:

    :::bash
    virtualenv <name>
    
Activate the virtual environment:

    :::bash
    source <path>/<name>/bin/activate