# reads in a file, returns a list of directories
import re
class index_file:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        self.base = ""

    def popFileContents(self):

        filename = self.filename
        sh_list = []
        print("Reading from: " + filename)

        #open stream
        f = open(filename)

        #grab the header
        common_path = f.readline()
        self.base = common_path.strip()

        #increment through the file
        for line in f:
            #add base common_path
            target = line.strip()
            target = self.base + target[1:]
            #add element to list
            sh_list.append(target)
            print(target)

        f.close()
        self.lines = sh_list

    def getFileContentsAsDictionary(self):
        sh_dict = { }
        self.popFileContents()

        #alias the list of paths
        paths = self.lines

        for path in paths:
            # strip off thje base path for eath path
            relativeDirectory = path.replace(self.base, "")
            print (relativeDirectory[1:])
            # now it's left with just the game/file.sh

            dirSplit = re.split("\/", relativeDirectory[1:], 1)
            #print(dirSplit)
            title = dirSplit[0]
            #game = key, executable is value
            if title not in sh_dict:
                sh_dict[title] = path
            else:
                #title already exists in dictionary
                sh_dict[title+"_alt"] = path

        print (sh_dict)
        return sh_dict
