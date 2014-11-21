#!/bin/bash
#Author of this file is JACQUES COETZEE

#Make sure that you are running kali linux
#we will use Kali as a base platform
#Run This file to make sure your tools are up to date and that the missing ones are installed and updated.


#Input from PETER KIM from his book "The HAcker Playbook"

#Global Vars
cwd=$(pwd)

#define some vars for formatting
txtreset="\e[0m"
txtylw='\e[0;33m'
txtbold='\e[1;31m'
txtgrn='\e[0;32m'

clear
#Give the user some input as to what the hell is happening :)
echo -e "${txtgrn}Thanks for using SHFT  "
echo -e "Author: Jacques Coetzee "
echo -e "Attempting to update your pen test lab. ${txtylw}"

#-------------------------------------------------------------------
# UPDATE SECTION
#-------------------------------------------------------------------

#first update Kali
echo ""
echo -e "${txtgrn}Updating APT.... ${txtylw}"
apt-get update
wait

#update the Kali Distribution
echo ""
echo -e "${txtgrn}Updating your Kali Distribution ${txtylw}"
apt-get dist-upgrade
wait



#update/install SMBExec - Not currently availalbe in APT-GET so we must clone
echo ""
echo -e "${txtgrn}Installing/Updating SMBExec ${txtylw}"

dir="/opt/smbexec/"

if [ -d "$dir" -a ! -h "$dir" ]
then
  echo -e "${txtgrn}${dir} found will update from github ${txtylw}"
  cd ${dir} && git pull .
	wait
  echo -e "${txtgrn}SMBExec NEEDS TO BE COMPILE THE BINARIES. PLEASE SELECT NUMBER FOUR (4) FROM THE SMBExec MENU WHEN STARTING UP... ${txtylw}"
  echo -e "${txtgrn}THEN NUMBER FIVE (5) TO EXIT ${txtylw}"
  read -p "Press any key to Continue..."
  ./install.sh
	cd ${cwd}
else
  echo -e "${txtgrn}${dir} not found. Will clone from github.com ${txtylw}"
  cd /opt
  git clone https://github.com/brav0hax/smbexec.git
  wait
	cd smbexec
  echo -e "${txtgrn}SMBExec NEEDS TO BE INSTALLED. PLEASE SELECT NUMBER ONE (1) FROM THE SMBExec MENU WHEN STARTING UP... ${txtylw}"
  echo -e "${txtgrn}AFTER THAT SELECT NUMBER FOUR (4) TO COMPILE THE LIBRARIES${txtylw}"
  echo -e "${txtgrn}AFTER THAT SELECT NUMBER FIVE (5) TO EXIT${txtylw}"
  read -p "Press any key to Continue..."
  ./install.sh
	wait
	cd ${cwd}
fi



#update/install VEIL - Evasion - Not currently WORKING in APT-GET so we must clone
echo ""
echo -e "${txtgrn}Installing/Updating VEIL-EVASION ${txtylw}"
dir="/opt/Veil-Evasion"
if [ -d "$dir" -a ! -h "$dir" ]
then
  echo -e "${txtgrn}${dir} found will update from github ${txtylw}"
  cd ${dir} && git pull .
	wait
	cd ${cwd}
else
  echo -e "${txtgrn}${dir} not found. Will clone from github.com ${txtylw}"
  cd /opt
  git clone https://github.com/Veil-Framework/Veil-Evasion.git
  wait
	cd Veil-Evasion/setup/
  ./setup.sh
	wait
	cd ${cwd}
fi



#update/install WCE - Windows Credential Editor
echo ""
echo -e "${txtgrn}Installing/Updating WCE (Windows Credential Editor)"
apt-get install wce
#create a symbolink link in /usr/bin for easy execution
ln -s /usr/share/wce/wce32.exe /usr/bin/wce32bit.exe
ln -s /usr/share/wce/wce64.exe /usr/bin/wce64bit.exe
wait



#update/install mimikatz
echo ""
echo -e "${txtgrn}Installing/Updating mimikatz"
apt-get install mimikatz
wait

#update/install burpsuite
echo ""
echo -e "${txtgrn}Installing/Updating burpsuite"
apt-get install burpsuite
wait



#update/install PeepingTom - Not currently availalbe in APT-GET so we must clone
echo ""
echo -e "${txtgrn}Installing/Updating PeepingTom ${txtylw}"
dir="/opt/peepingtom/"
if [ -d "$dir" -a ! -h "$dir" ]
then
  echo -e "${txtgrn}${dir} found will update from github ${txtylw}"
  cd ${dir} && git pull .
	cd ${cwd}
else
  echo -e "${txtgrn}${dir} not found. Will clone from github.com ${txtylw}"
  cd /opt
  git clone https://bitbucket.org/LaNMaSteR53/peepingtom.git
  wait
	cd peepingtom 
	wget https://gist.github.com/nopslider/5984316/raw/423b02c53d225fe8dfb4e2df9a20bc800cc78e2c/gnmap.pl
  wait
	wget https://phantomjs.googlecode.com/files/phantomjs-1.9.2-linux-i686.tar.bz2
	wait
  tar -xvjf phantomjs-1.9.2-linux-i686.tar.bz2
  wait
	cp ./phantomjs-1.9.2-linux-i686/bin/phantomjs .
  wait
	cd ${cwd}
fi



#update/install nmap
echo ""
echo -e "${txtgrn}Installing/Updating NMap${txtylw}"
apt-get install nmap
wait
cd /usr/share/nmap/scripts/
wget https://raw.github.com/hdm/scan-tools/master/nse/banner-plus.nse
cd ${cwd}


#update/install powersploit
echo ""
echo -e "${txtgrn}Installing/Updating Powersploit${txtylw}"
apt-get install powersploit
wait
cd /usr/share/powersploit/
file="StartListener.py"
if [! -f "$file" ]
then
	wget https://raw.github.com/obscuresec/random/master/StartListener.py
fi
wait
file="ps_encoder.py"
if [! -f "$file" ]
then
	wget https://raw.github.com/darkoperator/powershell_scripts/master/ps_encoder.py
fi
wait
cd ${cwd}

#update/install responder
echo ""
echo -e "${txtgrn}Installing/Updating Responder${txtylw}"
apt-get install responder
wait


#update/install SET
echo ""
echo -e "${txtgrn}Installing/Updating SET (Social Engineering Toolkit)${txtylw}"
apt-get install set
wait



#update/install BypassUAC
#echo ""
#echo -e "${txtgrn}Installing/Updating bypassuac ${txtylw}"
#file="/opt/metasploit/apps/pro/msf/scripts/meterpreter/bypassuac.rb"
#if [ ! -f "$file" ]
#then
#  wget http://www.secmania.com/files/bypassuac.zip
#  unzip bypassuac.zip
#  cp bypassuac/bypassuac.rb /opt/metasploit/apps/pro/msf/scripts/meterpreter/
#  mv bypassuac/uac/ /opt/metasploit/apps/pro/msf3/data/exploits/
#fi
#cd ${cwd}



#update/install BeEF
echo ""
echo -e "${txtgrn}Installing/Updating Beef-xss${txtylw}"
apt-get install beef-xss
wait


#update/install Fuzzing List
echo ""
echo -e "${txtgrn}Installing/Updating Fuzzing Lists ${txtylw}"
dir="/opt/SecLists/"
if [ -d "$dir" -a ! -h "$dir" ]
then
  echo -e "${txtgrn}${dir} found will update from github ${txtylw}"
  cd ${dir} && git pull .
	cd ${cwd}
else
  echo -e "${txtgrn}${dir} not found. Will clone from github.com ${txtylw}"
  cd /opt
  git clone https://github.com/danielmiessler/SecLists.git
  wait
	cd ${cwd}
fi


#update/install Discover from Lee Baird - we must clone
echo ""
echo -e "${txtgrn}Installing/Updating Discover${txtylw}"
dir="/opt/discover/"
if [ -d "$dir" -a ! -h "$dir" ]
then
  echo -e "${txtgrn}${dir} found will update from github ${txtylw}"
  cd ${dir} && git pull .
	cd ${cwd}
else
  echo -e "${txtgrn}${dir} not found. Will clone from github.com ${txtylw}"
  cd /opt
  git clone https://github.com/leebaird/discover.git
  wait
	cd discover 
  ./setup.sh
	wait
	cd ${cwd}
fi


#------------------------------------------------------------------------------------------------
# STARTUP SECTION
#------------------------------------------------------------------------------------------------

#Start Postgresql
echo ""
echo -e "${txtgrn}Start PostgreSQL ${txtylw}"
service postgresql start
wait

#Start Metasploit
echo ""
echo -e "${txtgrn}Start Metasploit ${txtylw}"
service metasploit start
wait


#FOR THE USER
echo ""
echo -e "${txtgrn}HERE ARE SOME THINGS YOU NEED TO DO YOURSELF ${txtreset}"
echo ""
echo -e "${txtgrn}Download the Crackstation-human-only passwordlist here: ${txtreset}"
echo -e "${txtgrn}https://mega.co.nz/#!3VZiEJ4L!TitrTiiwygI2I_7V2bRWBH6rOqlcJ14tSjss2qR5dq ${txtreset}"
echo ""


#Finally we are done :)
echo ""
echo -e "${txtgrn}SHFT is now ready to rock and roll ${txtreset}"


#update flamerobin
echo ""
echo -e "${txtgrn}Updating flamerobin ${txtylw}"
apt-get install flamerobin
wait
