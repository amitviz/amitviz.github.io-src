Title: Spin down hard disk drives in Linux
Date: 2016-10-30
Category: Notes
Tags: code, linux
Slug: 
Authors: Amit

Using `hdparm`, to determine the current state: 

    :::bash
    hdparm -B /dev/sda

To set the parameters: 

    :::bash
    hdparm -B 127 -S 36 -M /dev/sda
    
* `-B` sets advanced pover management: values below 128 permit spin-down
* `-S` sets the spin-down time, in multiples of 5 seconds. 36 here represents 3 minutes
* `-M` sets Automatic Acoustic Management (if the feature is supported on the HDD)

To set these values persistently, add a `udev` rule, e.g. `/etc/udev/rules.d/50-hdparm.rules`:

    :::bash
    ACTION=="add", SUBSYSTEM=="block", KERNEL=="sda", RUN+="/sbin/hdparm -B 127 -S 36 -M /dev/sda"

This will set the APM level on boot, but it might get reset after sleeping. To get around this, add a systemd service `/etc/systemd/system/apm.service`:

    :::bash
    [Unit]
    Description=Local system resume actions
    After=suspend.target hybrid-sleep.target hibernate.target

    [Service]
    Type=simple
    ExecStart=/sbin/hdparm -B 127 -S 36 -M /dev/sda

    [Install]
    WantedBy=sleep.target

Then either start the service (for this session):

    :::bash
    systemctl start apm.service

or enable the service to automatically start for all sessions:

    :::bash
    systemctl enable apm.service
