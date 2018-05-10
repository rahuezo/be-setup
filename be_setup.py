import tkFileDialog as fd
import os

DIRS = [
    'Research',
    'BE Ready Files',
    'BEA Files',
    'Email Syntax',
    'Sales Navigator Company Parsing',
    'Triage Form'
]


project_home = fd.askdirectory(title="Choose project home directory")
project_name = raw_input("Enter project name (e.g. Carbonite Test Project): ")

home_path = os.path.join(project_home, project_name)

for directory in DIRS: 
    dir_path = os.path.join(home_path, directory)

    if not os.path.exists(dir_path): 
        os.makedirs(dir_path)
        print "Created {}".format(dir_path)
    else:
        print "{} already exists!".format(dir_path)
