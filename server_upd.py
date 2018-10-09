#!/bin/python
#
# Script to check for server updates and create a JIRA ticket on JIRA Service Desk
# Change : Add variables, remove txt files and search for updates.
# Created by : Eduardo Rocha
# Version : 1.0
# Modified : 10.09.2018
#

import os, shutil, socket, subprocess, shlex

# Declare variables

description="h1.{color:#ff0000}" + socket.gethostname() + ".esc13.net{color}" + "\\u000a"
folder_path="/home/erocha"
cmd_line='rm ' + '-f' + ' ' + folder_path + '/' + 'bashscripts' + '/' + '*.txt'

os.system(cmd_line)

os.system('sudo yum update --assumeno > /home/erocha/bashscripts/centos-update.txt')
os.system('sudo yum update --assumeno | grep "Upgrade" > /home/erocha/bashscripts/updates.txt')


