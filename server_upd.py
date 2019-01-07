#!/bin/python
#
# Script to check for server updates and create a JIRA ticket on JIRA Service Desk
# Change : Add functions to read and create files, add a log file
# Created by : Eduardo Rocha
# Version : 1.5
# Modified : 01.07.2019
#

import os, shutil, socket, subprocess, shlex, datetime

# Declare variables

description="h1.{color:#ff0000}" + socket.gethostname() + ".esc13.net{color}" + "\\u000a"
folder_path="/home/erocha"
grep_cmd='grep "Upgrade" > '
cmd_yum="sudo yum update --assumeno >" + folder_path + "/bashscripts/centos-update.txt"
cmd_yum_grep="sudo yum update --assumeno | " + grep_cmd + folder_path + "/bashscripts/updates.txt"
cmd_line='rm ' + '-f' + ' ' + folder_path + '/' + 'bashscripts' + '/' + '*.txt'


def read_file():
    global description

    # Open the file and read the contents
    f=open(folder_path + "/bashscripts/ticket.txt", "r")
    # Readlines reads the individual line into a list
    fl =f.readlines()
    for file_row in fl:
       description=description + file_row + "\u000a"
    f.close()

return

def create_ticket(summary):
    # Create the JIRA ticket in JSON format

    global description

    f=open(folder_path + "/bashscripts/jira.txt","w+")
    f.write("{ \r\n")
    f.write('"fields": {\r\n')
    f.write('"project": {\r\n')
    f.write('"key": "ITHELP"\r\n')
    f.write("},\r\n")
    f.write('"summary":' + '"' + summary + '"' + ',\r\n')
    f.write('"description":' + '"' + description + '"' + ',\r\n')
    f.write('"issuetype": {\r\n')
    f.write('"name": "Task"\r\n')
    f.write("}\r\n")
    f.write("}\r\n")
    f.write("}\r\n")

    f.close()
return

def log_file(args):
    # Log the event

    now=datetime.datetime.now()
    date_log=now.strftime("%c")
    flog=open(folder_path + "/bashscripts/updates.log","a+")
    #flog.write(os.system('date') + args)
    flog.write(date_log + args + '\r\n')
    flog.close()

return    


# Main function

def main():
    os.system(cmd_line)

    os.system(cmd_yum)
    os.system(cmd_yum_grep)

    if (os.stat('/home/erocha/bashscripts/updates.txt').st_size > 0):
        os.system('/home/erocha/bashscripts/ticket.sh')
        summary="Server Updates. -> " + socket.getfqdn()
        read_file()
        create_ticket(summary)
        log_file(" Regular update")
    else:
        log_file(" No updates")


# Main 
if __name__ == "__main__":
     main()



