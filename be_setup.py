import os, sys, time

BASE_DIRS = [
    'CSMS and Reports',
    'Email Campaigns',
    'Lead Projects'
]

DIRS = [    
    ['Lead Projects/{}/0 Resources', 'notes.txt' ],
    'Lead Projects/{}/1 Intake Form',
    'Lead Projects/{}/2 Research',
    'Lead Projects/{}/3 Sales Navigator Company Parsing',
    'Lead Projects/{}/4 Email Syntax',
    'Lead Projects/{}/5 BE Ready Files',
    'Lead Projects/{}/6 BEA Files',    
    'Lead Projects/{}/7 Final Files LinkedIn',
]


project_home = r'../../Projects'

project_name = raw_input("\nEnter project name (e.g. Carbonite Test Project): ")

if not project_name: 
    print "\nNo project name given. Goodbye!\n"
    sys.exit()

for base_directory in BASE_DIRS: 
    dir_path = os.path.join(project_home, base_directory)

    if not os.path.exists(dir_path): 
        os.makedirs(dir_path)
        print "Created {}".format(dir_path)
    else:
        print "{} already exists!".format(dir_path)

home_path = os.path.join(project_home, project_name)

for directory in DIRS:
    if type(directory) == list:
        dir_path = os.path.join(project_home, directory[0].format(project_name))
    else: 
        dir_path = os.path.join(project_home, directory.format(project_name))

    if not os.path.exists(dir_path): 
        os.makedirs(dir_path)
        print "Created {}".format(dir_path)
    else:
        print "{} already exists!".format(dir_path)
    
    if type(directory) == list:
        with open(os.path.join(dir_path, directory[-1]), 'w') as f: 
            f.write("{} Notes\n\n".format(project_name))
            f.write("-"*6 + "      Timing      " + "-"*6)
            f.write("\n\n")
            f.write("-"*6 + " FrontEnd Queries " + "-"*6)
            f.write("\n\n")
            f.write("-"*6 + "    Title List    " + "-"*6)
            f.write("\n\n")
            f.write("-"*3 + " Server Search Companies " + "-"*2)

    time.sleep(0.2)

os.startfile(os.path.join(project_home, 'Lead Projects', project_name))
