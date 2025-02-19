#!/usr/bin/env python3


import csv
import os
import re
import subprocess

subprocess.call('clear' )

print(" ")
print(" ")
print("Script written by: Mina Ramez Farag")
print("")
print("       ***************************************")
print("       ****Linux - Users adding Automation****")
print("       ***************************************")
print("")
print("User data is typed as following:")
print("Username:password | password type")
print("")

default_password= "password"

#check if a group exists or not, and to add it if not. 
def check_group( group_name):
    try:
        subprocess.check_output(['getent', 'group', group_name] )
    except subprocess.CalledProcessError:
        subprocess.call([ 'groupadd', group_name])

#read the csv file in the given directory. 
with open('linux_users.csv','r') as file :
    csv_reader =csv.reader( file )
    next(csv_reader )
    
    for row in csv_reader:
        if all(row[:6] ):
            first_name= row[ 2].lower()
            last_name= re.sub( r'[^\w\s]','', row[1]).lower( ) 
            username = first_name[0 ] +last_name
            
            #function that checks for duplicate users
            count=1
            while  True:
                try:
                    subprocess.check_output( ['getent', 'passwd', username])
                    count+= 1
                    username= first_name[0 ]+ last_name+ str(count)
                except subprocess.CalledProcessError:
                    break
            
            department =row[5]
            home_dir =os.path.join('/home', department, username)
            
            if not os.path.exists( os.path.join('/home', department)):
                subprocess.call( ['mkdir', os.path.join('/home',department)])
            
            group_name = row[6 ] if row[6] else 'unnamedgroup'
            check_group( group_name)
            
            default_shell= '/bin/csh' if group_name =='office' else '/bin/bash'
            
            try:
                subprocess.call(['useradd', '-m', '-d' , home_dir, '-s', default_shell, '-g', group_name, username])
            except subprocess.CalledProcessError:
                print(" ")
                print(f"User account {username} was not added due to an error.")
            
            subprocess.call(['echo',f"{username}:{default_password}", '|', 'chpasswd'] )
            subprocess.call(['passwd', '-e', username])
            print("")
        else:
            print(username, ": account was not added due to missing information.")
            print(" ")