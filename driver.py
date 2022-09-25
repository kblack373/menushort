
#reads in a file, creates menu shortcuts for steam games

import sys
import filereader
import shwriter
import getopt

argsList = sys.argv[1:]

options = "hmo:"
long_options = ["File", "Path", "Help"]
blnCustomFile = 0
blnShowOutput = 0

filename = ""

try:
    args, vals = getopt.getopt(argsList, options, long_options)
    for currentArgument, currentValue in args:

        if currentArgument in ("-h", "--Help"):
            print ("Displaying Help")
            ## TODO: write display help
        elif currentArgument in ("-f", "--file"):
            print ("File: " + currentValue)
            filename = currentValue
            blnCustomFile = 1
        elif currentArgument in ("-o", "--output"):
            print ("Showing output")
            blnShowOutput = 1

except getopt.error as err:
    print (str(err))

if blnCustomFile == 0:
    filename = "/home/kb/Documents/steam_sh"
    print ("File: " + filename)

reader = filereader.index_file(filename)
#sh_list = reader.getFileContents()
sh_dict = reader.getFileContentsAsDictionary()
if blnShowOutput == 1:
    print (sh_dict)
