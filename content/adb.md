Title: adb backup
Date: 2013-01-22
Category: Notes
Tags: code, android
Slug: 
Authors: Amit

    #!bash
    adb backup [-f <file>] [-apk|-noapk] [-shared|-noshared] [-all] [-system|nosystem] [<packages...>]

-f specify filename

-apk|noapk include apks

-all backup all apps (rather than specify individual packages)

-shared|noshared backup shared storage partition (i.e. sdcard)

-system include system packages

<packages> specify package names to backup


To backup and restore to a different ROM, usually:

    #!bash
    abd backup -f ~/backup.ab -apk -all -noshared -nosystem

To restore:

    #!bash
    adb restore ~/backup.ab

Convert to tar (only if backup was unencrypted):

    #!bash
    dd if=backup.ab bs=24 skip=1 | openssl zlip -d > backup.tar
    
