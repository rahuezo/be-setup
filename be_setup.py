from Tkinter import *


import tkFileDialog as fd
import os, sys, time

root = Tk()
root.withdraw() # hide root

DIRS = [
    '2 Research',
    '5 BE Ready Files',
    '6 BEA Files',
    '4 Email Syntax',
    '3 Sales Navigator Company Parsing',
    '1 Triage Form'
]


project_home = fd.askdirectory(title="Choose project home directory")

if not project_home: 
    print "\nNo directory selected. Goodbye!\n"
    sys.exit()

project_name = raw_input("Enter project name (e.g. Carbonite Test Project): ")

if not project_name: 
    print "\nNo project name given. Goodbye!\n"
    sys.exit()

home_path = os.path.join(project_home, project_name)

for directory in DIRS: 
    dir_path = os.path.join(home_path, directory)

    if not os.path.exists(dir_path): 
        os.makedirs(dir_path)
        print "Created {}".format(dir_path)
    else:
        print "{} already exists!".format(dir_path)
    
    time.sleep(1)

os.startfile(home_path)
