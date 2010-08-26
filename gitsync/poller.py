from gitsync.gitwrapper import GitWrapper

class Poller:
    def __init__(self, config={}):
        self.config = config

    def run(self):
        #
        # getting the repo
        #
        repo = GitWrapper("/", config=self.config)
        
        #
        # setting the ignores
        #
        repo.set_ignores()

        #
        # now add what we want to watch
        #
        repo.do_monitor()
