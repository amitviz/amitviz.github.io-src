Title: Anaconda environments
Date: 2016-10-10
Category: Notes
Tags: python, conda, virtualenv
Slug: 
Authors: Amit

[Anaconda][url] is a Python distribution and package manager that might be a bit nicer than using `virtualenv`s and `pip`.

[url]: https://www.continuum.io/downloads#linux

To set up a new environment using Anaconda:

    #!bash
    conda create --name <envname> python=3.5

The environment is created in the Anaconda installation directory. To activate and deactivate the environment:

    #!bash
    source activate <envname>
    source deactivate <envname>

In the terminal, the prompt will be preceded by `<envname>` when the environment is active.

If you want to delete the environment, find out the name of it and remove:

    #!bash
    conda info --envs
    conda remove --name <envname> --all

The useful thing about Anaconda environments is that they can be exported and shared with code: 

    #!bash
    conda env export > environment.yml
    
Then, someone else doing development on the same code base can set up an identical environment: 

    #!bash
    conda env create -f environment.yml

When the environment is active, packages can be searched for and installed as follows:

    #!bash
    conda search numpy
    conda install numpy

The packages within the Anaconda environment can be listed by: 

    #!bash
    conda list

To update any of the packages:

    #!bash
    conda update <packagename>

where `<packagename>` is any of the listed packages, including `python`.



