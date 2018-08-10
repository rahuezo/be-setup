import os, sys, time


DIRS = [
    ['0 Resources', 'notes.txt' ],
    '1 Intake Form',
    '2 Research',
    '3 Sales Navigator Company Parsing',
    '4 Email Syntax',
    '5 BE Ready Files',
    '6 BEA Files',    
    '7 Final Files LinkedIn',
    '8 Final Files Sans LinkedIn',
]


project_home = r'../../Projects'

project_name = raw_input("\nEnter project name (e.g. Carbonite Test Project): ")

if not project_name: 
    print "\nNo project name given. Goodbye!\n"
    sys.exit()

home_path = os.path.join(project_home, project_name)

for directory in DIRS:
    if type(directory) == list:
        dir_path = os.path.join(home_path, directory[0])
    else: 
        dir_path = os.path.join(home_path, directory)

    if not os.path.exists(dir_path): 
        os.makedirs(dir_path)
        print "Created {}".format(dir_path)
    else:
        print "{} already exists!".format(dir_path)
    
    if type(directory) == list:
        with open(os.path.join(dir_path, directory[-1]), 'w') as f: 
            f.write("{} Notes\n\n".format(project_name))
            f.write("-"*6 + " Timing " + "-"*6)
            f.write("\n\n")
            f.write("-"*6 + " BE Parameters/Resources " + "-"*6)

    time.sleep(0.2)

os.startfile(home_path)
