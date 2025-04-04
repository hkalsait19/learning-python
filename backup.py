
import shutil
import datetime
import os

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz") ## f --> f-string --> formatted string

    shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source) ## zip also works

source = "/Users/shraddha/Documents/python-worshop-practice"
destination = "/Users/shraddha/Documents/python-worshop-practice/backup"
backup_files(source,destination)