
#reads in a file, creates menu shortcuts for steam games

import sys
import filereader
import getopt

argsList = sys.argv[1:]

options = "hmo:"
long_options = ["File", "Path", "Help"]
customFile = 0

filename = ""

try:
    args, vals = getopt.getopt(argsList, options, long_options)
    for currentArgument, currentValue in args:

        if currentArgument in ("-h", "--Help"):
            print ("Displaying Help")
            ## TODO: write display help
        elif currentArgument in ("f", "--file"):
            print ("File: " + currentValue)
            filename = currentValue
            customFile = 1

except getopt.error as err:
    print (str(err))

if customFile == 0:
    filename = "/home/kb/Documents/steam_sh"
    print ("File: " + filename)

reader = filereader.index_file(filename)

#sh_list = reader.getFileContents()
reader.getFileContentsAsDictionary()
