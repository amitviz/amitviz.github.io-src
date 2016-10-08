Title: virtualenv and VTK
Date: 2016-10-07
Category: Notes
Tags: code, python
Slug: vtk
Authors: Amit
Summary: How to get VTK working in a virtualenv

For whatever reason, I can't get [VTK] [vtk] to install in my virtualenv. So, the horrible hack I am using is to symlink the system package to my virtualenv:


[vtk]: http://www.vtk.org/Wiki/VTK/Examples/Python
    
    :::bash
    ln -s /usr/lib64/python3.5/site-packages/vtk ~/PATH/TO/VIRTUALENV/lib64/python3.5/site-packages/
