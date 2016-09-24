Title: Git basics
Date: 2011-11-29
Category: Notes
Tags: code
Slug: 
Authors: Amit

create local repo:

    git init
    
add files to version tracking ('stage'):

    git add .
    
commit files to repo:

    git commit -m "Comment"

automatically commit modified files:

    git commit -a (does NOT add new files)

add changed files (inc. deleted files): 

    git add -A .

list branches: 

    git branch (default is master)

create new branch: 

    git branch <branchname>

switch to branch: 

    git checkout <branchname>

push to remote repo: 

    git push git://*.git

define a remote repo: 

    git remote add <reponame> git://*.git (default repo name is origin)

push to remote repo: 

    git push <reponame>

push to a specific branch: 

    git push <reponame> <branchname>

alt: 

    git push <reponame> <localbranchname>:<remotebranchname>

list remote repos: 

    git remote

clone repo: 

    git clone git://*.git

create local branch clone of remote branch: 

    git checkout -b <branchname> origin/<remotebranchname>

list all branches (inc remote): 

    git branch -a

get the latest updates from the remote repo: 

    git pull <reponame>
