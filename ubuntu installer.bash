#!/bin/bash
#installer for the EVL Suite GUI
##########################################
#ESTABLISH SUDO RIGHTS FOR INSTALL 
echo " This program requires sudo rights for install , please enter password when prompted" 
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@" 
###########################################
#initialize install 
while read  [[ $INSTALL != Y || $INSTALL != ]] do; 
	read -p "This will install the EVL-Suite software, would you like to continue? Enter Y or N to continue" INSTALL;
		if [ $INSTALL = Y ] ; then 
			echo " Proceeding With EVL-Suite INSTALL"
			continue 
		else [ $INSTALL = N ] ; then
			exit 2 
###########################################

###########################################
#verify prequisite installs
echo "verifying prequisite items" 
sleep 2
	# Check the system Python INSTALL
		#establich desired binaries to identify 
	TARGETBINS=python3 
	PACKAGES= python3
		#generate VAR of : list all env path routes |  edit list into readable format for future command by removing : and replacing with a space
	ENVLIST=$(echo $PATH 2>/dev/null |tr ":" " ")
		#scan env paths for presence of desired command binary, by listing all binaries with ls , piping errors to null , then filtering output with grep set for 1 line only with ^startswith and $endswith to isolate command
	PYSCAN=$( ls $ENVLIST 2>/dev/null | grep -m 1 ^"$TARGETBIN"$ )
		#run check on output to verify if desired program installed
	if [ $PYSCAN != $TARGETBINS ] ; then 
			echo "the presence of $TARGETBINS was not found , proceeding to install $TARGETBINS " 
			sleep 2
			sudo apt install -y ${PACKAGES}
			echo "dependency installs completed"
	else ; then
			sleep 2
			echo "${TARGETBINS} have been identified as installed, proceeding. "

###############################################

#python execution of EVL-Suite
	#isolate binary absolute path of python3 using which and assign to variable
	PYBIN=$(which python3)
	#execute in python shell for execute python program 
	/usr/bin/python EVL-Suite.python
	

			
	
		 
	
