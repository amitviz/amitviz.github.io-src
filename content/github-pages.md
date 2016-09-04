Title: Github pages
Date: 2015-11-08
Modified: 2015-11-09
Category: Notes
Tags: code, pelican, git
Slug: github-pages
Authors: Amit

How to sync this blog to Github

Now that some of the basic functionality of the blog is up and running, I have started to investigate hosting it. I've chosen Github, for the fact that it's simple and free. The way I do this is documented here.

The local folder has been set up as a git repository. [ghp-import] [ghpi] is installed:

[ghpi]: https://github.com/davisp/ghp-import

    :::bash
    pip install ghp-import

Do the usual initialization and commit:

    :::bash
    git add .
    git commit -m "<message>"

Then, use `ghp-import` to add files to the branch gh-pages, then push to Github:

    :::bash
    ghp-import output
    git push git@github.com:amitviz/amitviz.github.io.git gh-pages:master

To be perfectly honest, this seems like a bit much effort. What I should do at some point is to add these commands to the makefile to automate as much as possible.