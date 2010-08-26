#!/usr/bin/env python
 
import os
import sys
import ConfigParser

#
# ignore warnings
#
import warnings
warnings.filterwarnings("ignore")

from gitsync.poller import Poller

#
# config dictionary
#
config = {}
 
if __name__ == "__main__":
    
    #
    # load up the config
    #
    path = os.path.dirname(os.path.realpath(__file__))
    c = ConfigParser.ConfigParser()

    if os.path.exists("/etc/gitsync/gitsync.conf"):
        c.read("/etc/gitsync/gitsync.conf")
    else:
        c.read(path +"gitsync.conf")

    
    #
    # load the config
    #
    config = {}
    config['githost'] = c.get('MAIN', 'githost')
    config['debug'] = c.getboolean('MAIN', 'debug')

    poller = Poller(config)
    poller.run()
    
    