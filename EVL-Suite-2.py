#!/usr/bin/python3 


{ class EVL_PY_IMPORTS1:
########################################################
# ##########IMPORTS TO PREPARE ENVIORNMENT
############ADD ITEMS AS REQUIRED 
########				#will need to circle back and resolve potential errors and codes
#########################################################
######$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###########


                        {               # funtion for Tkinter import , Tkinter is a GUI aspect of python 
                                def EVL_imports=_imp(funct):
                                                        #Tkinter Graphical Interface
                                        import Tkinter 
					from Tkinter import *
                                                        #https://github.com/fabric/fabric
							#pip install fabric
                        EOF}
	
                        {               #function for import os and sys as a pair. OS allow's python to interact with systems it does not know and talk to them 
                                def EVL_OS(funct):         
                                                        #OS Miscellaneous operating system interfaces
                                        import os
                                        from os import *
                                                        #comes with python
                         EOF}
				
                        {                                #SYS System-specific parameters and functions
                                 def EVL_SYS
                                        import sys 
                                        from sys import *
                                                        #comes with python 
                        EOF }
				
                        {               #psutil is a light weight program that brings the logging , coloring , and syntax of errors from one platfporm to another
                                def EVL_psutil_imp
                                                        #PSUtils , process specific tools for admins
                                        import psutil
                                        from prutil import *
                                                       #sudo pip install psutil
                                                        #https://github.com/giampaolo/psutil/blob/master/INSTALL.rst
                         EOF} 
                        
  EOF }
	
{class EVL_PY_IMPORTS2
#############################################
####Future activations
############################################ 
			
                        
                       {                   #Fabric CLI and remote administration suite
                                def EVL_FABRIC
                                               #import fabric
                                                #from fabric import * 
						# pip install fabric
						#https://github.com/fabric/fabric
                        EOF }
                        
                        {                       #Click CLI creation and fine tuned script management
                                def EVL_CLICK
			
                                                #import click
                                                #from click import * 
                                                # pip3 install 
                         EOF}
			
			{                       #Salt remote node and systems management with automation capability
                                def EVL_SALT
                                                #import salt
                                                #from salt import *
                                                # https://ansible-cn.readthedocs.io/en/stable/topics/installation/index.html 
                                                #pip3 install salt 
                                                #installs to unpathed location , add /home/luciphronnaxtel/.local/bin
			EOF}
			
                        {                       #Python DB Sqlite3 libraries
                                def EVL_SQLITE3
                                                #import sqlite3
                                                #from sqlite3 import * 
                                                #included with python 3 base
			EOF}
			
                        {                       #PYBashutils logging and color config for python fromhttps://www.pyinstaller.org/ bash 
                                def EVL_BASHUTILS
                                                #import bashutils
                                                #from bashutils import *
						#https://github.com/scivision/pybashutils "github main page"
                                                #https://github.com/scivision/pybashutils.git "for use with git clone" 
			EOF}
                        
EOF}
	#############################################
	####Notes FOR INSTALLER COMPILATION 
	############################################
			
                                                #REQUIREMENTS FOR INSTALLATION COMPILER
                                                        #https://github.com/pyinstaller/pyinstaller/blob/e20e74c03768d432d48665b8ef1e02511b16e4be/doc/requirements.rst
                                                #COMPILED USING 
                                                        #https://www.pyinstaller.org/
                                                #PIP will be required install for installer application
                                                        #sudo apt update ; sudo apt upgrade
                                                        #sudo apt install python3-pip
						
EOF}
			
                        
##############################################################
####### PREP MIN SYSTEM REQ CAPAB ILITY AND DEPENDENCIES 
####### PERFORM IN 2 STEPS , 1=LEAN FOR UNIVERSAL INSTALLER 2= LOAD IT UP FROM THE COURCE
################################################################



{ class EVL_DEPLS1
##################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$########
####### DEPENDENCIES & INSTALL PREP & INSTALL PHASE 1
####################################################################

                        {                       #SYSTEM ENVIORNMENT TO CHECK IF TASKS ARE POSSIBLE 
                                def  EVL_DEPLS1_CRITICAL                       
                                                 #populate variable of criticals
                                        DEPLS1_CRITICAL = ('aptitude', 'pip3', 'curl', 'tar')
                                 

                        EOF} 
                
                        {                       ##LEVEL 1 priority dependencies 
                                 def  EVL_DEPLS1_NORMAL    
                                                #List all primary dependencies for phase 1 install 
                                        DEPLS1_NORMAL = [ 'psutil', ' python3', 'python3-tk', 'python3-tk-dbg', 'python3-tksnack',' idle3', 'reptyr', 'python3.9-examples', 'pythonpy', 'python3.9-doc',  'python3.9-dbg', 'python3.9', 'python3.8',  'python3.8-examples', 'python3', '
'python-pip-whl', 'git', 'salt', 'click', 'fabric'] 

                        EOF} 

                        {
                                def EVL_DEPLS1_DOCKER           

                                                ##DOCKER SWARM CAPABILITY DEPENDENCIES 
                                                #List all dependencies for the docker deployment with swarm intention
                                        DEPLS1_DOCKER = ['docker', 'docker.io', 'gnupg', 'apt-transport-https','ca-certificates ', 'lsb-release', 'groupadd', 'docker', 'chown', 'chmod' ]
                                              
_
{class EVL_DEPLS1_DEPSCAN
##############################################################
########## PHASE 1 PART 2 - scan all dependencies for their own dependencies
########## for surety of correct installs for install phase 
##############################################################











class Window(Frame):
    def  init (self, master=None):
        Frame.__init__(self, master)
        self.master = master
		
		
		root.geometry("500x100") #Width x Height

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
			fileMenu.add_command(label="Python Terminal", command=os.system("echo Hello from the other side!"))
		
			fileMenu.add_command(label="Exit", command=self.exitProgram)
        
	menu.add_cascade(label="File", menu=fileMenu)
		editMenu = Menu(menu)
			editMenu.add_command(label="Todo")
			editMenu.add_command(label="Todo")
			menu.add_cascade(label="Edit", menu=editMenu)

    def exitProgram(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("EVL-Suite")
root.mainloop()

id init
