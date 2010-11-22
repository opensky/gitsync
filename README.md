## Overview

This little python script is a way to keep a server's files in a versioning server like GIT.

It is pretty simple and straight forward.

## Requirements

Make sure git is installed

### Redhat/CentOS

    yum install git

## Install

Run the following

    git clone git://github.com/opensky/gitsync.git
    cd gitsync
    python setup.py build
    sudo python setup.py install

## GitServer Setup

## Running

You can now run the gitsync command

    gitsync

Default configs are in the contrib directory. They can be placed in the /etc/gitsync dir. 
