import os
import sys
import subprocess

class GitWrapper:
    
    def __init__(self, path=None, config={}):
        self.config = config
        
        if path is None:
            return None
        
        #
        # check if the path is there
        #
        if not os.path.isdir(path):
            return None
        
        #
        # now check if we need to init the path
        #
        if not os.path.isdir(os.path.join(path, '.git')):
            #
            # lets init the repo
            #
            self.__init(path)

        
        
    def __init(self, path):
        #
        # init the repo
        #
        if self.config['debug']:
            print "---- Running git init now"
        
        status = self.__runGitCmd(["git", "init", path])
        
        if status > 0:
            print "Error initint the git repository on /"
            print "You need to run the application as root"
            sys.exit(2)
        
        #
        # grabbing server hostname
        #
        from socket import gethostname
        host = gethostname()
        
        #
        # setup the remote
        #
        self.__runGitCmd(["git", "remote", "add", "origin", "%s%s" % (self.config['githost'], host)])
    
    def __runGitCmd(self, args=[]):
        if self.config['debug']:
            print "------ [CMD] %s" % " ".join(args)
            
        p = subprocess.Popen(args, cwd="/", stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
        status = p.wait() 

        return status
    
    def __add(self, path):        
        if os.path.isfile(path) or os.path.isdir(path) or os.path.islink(path):
            self.__runGitCmd(["git", "add", path])

    def __commit(self):
        status = self.__runGitCmd(["git", "commit", "-a", "-m", "'changes'"])
        
        if status == 0:
            return True
        
        return False
    
    def __push(self):
        status = self.__runGitCmd(["git", "push", "origin", "master"])
        
        if status > 0:
            print "Push errored out"
            sys.exit(2)
    def set_ignores(self):
        try:
            f = open("/.git/info/exclude", "w")
        except:
            print "Cannot write to /.git/info/exclude"
            print "You need to run this as root"
            sys.exit(2)
        
        
        try:
            ignores = open('/etc/gitsync/git.ignore','r')
        except:
            print "Cannot load the file /etc/gitsync/git.ignore"
            print "Make sure it is a file"
            sys.exit(2)
        
        for line in ignores.readlines():
            line = line.strip()
            
            #
            # add it into the local gir ignore file
            #
            f.write(line + "\n")
            
        f.close()
        ignores.close()
            
    def do_monitor(self):
        try:
            montior = open('/etc/gitsync/git.monitor','r')
        except:
            print "Cannot load the file /etc/gitsync/git.monitor"
            print "Make sure it is a file"
            sys.exit(2)
            
        for line in montior.readlines():
            line = line.strip()
            self.__add(line)
            
        #
        # now do the commit if it fails nothing has changed so don't push
        #
        if self.__commit():
            #
            # now push the changes if there are any
            #
            status = self.__push()