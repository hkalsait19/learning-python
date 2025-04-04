
import os

# command = 'ls -l'
# command = 'du -sh'
# command = 'uptime'
# command = 'date'

# print(os.system(command))


def check_cpu(command):
    print(os.system(command))

# check_cpu('df -h')

def cehck_date(command):
    print(os.system(command))
#cehck_date('date')

def check_uptime(command):
    print(os.system(command))
#check_uptime('uptime')

def check_list_of_files_n_dir(command):
    print(os.system(command))
check_list_of_files_n_dir('ls -l')
