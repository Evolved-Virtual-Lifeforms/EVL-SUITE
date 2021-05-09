#!/bin/bash
#PYCHARM UBUNTU INSTALL
echo "are you sure you would like to continue with the installation of pycharm?"  
read -p "Y/N ?" LAUNCH
		if [ $LAUNCH = Y ]
				then 
						echo "initiating instalation sequence " 
		elif [ $LAUNCH = N ] 
				then 
						echo " canceling installation " 
									end 
		esle	
				echo " Please enter a valid command " 
							
						read -p "Y/N ?" LAUNCH
									if [ $LAUNCH = Y ]
												then 
														echo "initiating instalation sequence " 
									elif [ $LAUNCH = N ] 
												then 
														echo " canceling installation " 
																			end 
									else	
												then 				
														echo " Sorry EVL does not accept idots to use EVL tools" 
																			end
fi

 sudo apt install -y python2.7 python-pip python3.9-examples pythonpy python3.9-doc python3.9-dev python3.9-dbg python3.9 python3.8 python3.8-doc python3.8-examples python3.8-dev python3-pip python3-distutils
 sleep 1
 echo " initial python framework loaded for python 2.7, 3.0 , 3.8, 3.9 "
 sleep 1
 echo "Verifying and attemtping snap install " 
 sleep 1
 sudo apt install -y snap 
 sleep 1 
 echo " Pycharm professional license can be bought if you require the advanced features."
 echo " This can be done at the following link https://www.jetbrains.com/pycharm/buy/#commercial?billing=yearly"
 echo " If you require professional please proceed to the link and continue installation manually" 
 echo " EVL-PyCharm is for communoity version only" 
 read -p "would you like to continue? Y/N" COMMUNITY
		if [ $COMMUNITY = N ] 
			then 
					end
		elif [ $COMMUNITY = Y ] 
			then 
					echo " proceeding with install " 
		else 
			then 
				echo " PLEASE ENTER A VALID ENTRY Y/N " 
				
								read -p "would you like to continue? Y/N" COMMUNITY
										if [ $COMMUNITY = N ] 
											then 
													end
										elif [ $COMMUNITY = Y ] 
											then 
													echo " proceeding with install " 
										else 
											then 
													echo " terminating install EVL doesn't approve of idiots using its tools " 
																end
																
fi 
sudo apt update -y 
sudo apt upgrade -y 
sudo snap install pycharm-community --classic

				