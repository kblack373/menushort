# reads in a file, returns a list of directories

class index_file:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []

    def getFileContents(self):

        filename = self.filename
        sh_list = []
        print("Reading from: " + filename)

        #open stream
        f = open(filename)

        #grab the header
        common_path = f.readline()

        #increment through the file
        for line in f:
            #add base common_path
            target = ""
            target = common_path + line
            #add element to list
            sh_list.append(target)
            print(target)

        f.close()
        self.lines = sh_list

    def getFileContentsAsDictionary(self):
        
