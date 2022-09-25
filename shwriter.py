

class out_file:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

        def writeShorcutCreator(self, sh_dict):

            entries = sh_dict.items()

            fqn = self.filename + self.path

            f = open(fqn, "w")
            for entry in entries:
                #TODO: write command for creating MenuLibre Launchers
                
