import os ## Importing os module library into your code ## import is a keyword

print(os.system('df -h')) ## df -h command is used to check the 'disk space usage' in Linux OR MacOS
## print(os.system('dir')) ## dir command is used to check the disk space usage in Windows

print(os.system('uptime')) ## uptime command is used to check the 'system uptime' and load average in Linux OR MacOS
print(os.system('sysctl hw.memsize')) ## ram command is used to check the 'system RAM' MacOS
print(os.uname()) ## uname command is used to check the 'system information' in Linux OR MacOS



