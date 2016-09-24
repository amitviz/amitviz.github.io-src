Title: Offline email back-up using OfflineIMAP
Date: 2011-12-01
Category: Notes
Tags: code
Slug: 
Authors: Amit

[OfflineIMAP][url]
[url]: http://offlineimap.org/

    #!bash
    sudo zypper in offlineimap

Create ~/.offlineimaprc:

    #!
    [general]
    accounts = ACCOUNT_NAME1,ACCOUNT_NAME2
    maxsyncaccounts = 2
    socktimeout = 60

    [Account ACCOUNT_NAME1]
    localrepository = local-ACCOUNT_NAME1
    remoterepository = remote-ACCOUNT_NAME1

    [Account ACCOUNT_NAME2]
    localrepository = local-ACCOUNT_NAME2
    remoterepository = remote-ACCOUNT_NAME2

    [Repository local-ACCOUNT_NAME1]
    type = Maildir
    localfolders = YOUR_ARCHIVE_PATH1

    [Repository remote-ACCOUNT_NAME1]
    type = IMAP
    remotehost = imap.gmail.com
    remoteuser = YOUR_USER_NAME1
    remotepass = YOUR_PASSWORD1
    ssl = yes
    maxconnections = 1
    realdelete = no

    [Repository local-ACCOUNT_NAME2]
    type = Maildir
    localfolders = YOUR_ARCHIVE_PATH2

    [Repository remote-ACCOUNT_NAME2]
    type = IMAP
    remotehost = imap.gmail.com
    remoteuser = YOUR_USER_NAME2
    remotepass = YOUR_PASSWORD2
    ssl = yes
    maxconnections = 1
    realdelete = no

Setup a cron job to run periodically:

    #!bash
    offlineimap -u Noninteractive.Quiet
