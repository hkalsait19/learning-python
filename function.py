import os


# def check_cpu(command):
#     print(os.system(command))

# # check_cpu('df -h')

# def check_date(command):
#     print(os.system(command))
# #check_date('date')

# def check_uptime(command):
#     print(os.system(command))
# #check_uptime('uptime')

# def check_list_of_files_n_dir(command): ## defining a function
#     print(os.system(command))
# check_list_of_files_n_dir('ls -l') ## calling a function

# def check_ram(command):
#     return os.system(command)
# check_ram('sysctl hw.memsize')

##### best practice

def check_command(command): ## ONLY ONE time defining a function
    return os.system(command)

check_command('uptime') ## multiple time calling a function
check_command('date')
check_command('df -h')
check_command('du -sh')
check_command('ls -l')
check_command('sysctl hw.memsize')

##### date and time

import datetime

def date_check_time():
    #return datetime.datetime.now()
    return datetime.datetime.today()
print(date_check_time())