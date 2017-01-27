# FwConfigApp

This is a side project I have setup. It is nothing fancy, but it gave me a chance to play with buiding a GUI (using qtcreator) and building a project using the pycharm IDE (which I have grown to like).

Here is what I have done to install this project and get it running on Ubuntu 14.4:

1. Download and install PyCharm
  The instructions for downloading and installing pycharm can be found at https://www.jetbrains.com/pycharm

2. Install git
  - open a terminal on your ubuntu machine and type:
    - sudo apt-get install git

3. Clone this repo using pycharm
  The process for doing this as follows:
  - start pyCharm
  - if this is your first time starting pyCharm then select "Check out from Version Control" from the main slash window
  - if this is not your first time starting pyCharm, then close out all open projects which should take you to the main splash window from which you should select "Check out from Version Control"
  - from the "Check out from Version Control" drop menu select "Git". This will open the "Clone Repository" dialogue.
  - fill in the "Clone Repository" dialogue as follows:
    - set "Git Repository URL" to the URL provided by git for the FwConfigApp repository
      - pressing the "Test" button will verify that the URL is correct
    - set "Parent Directory" to the base directory where you store your pyCharm projects
      - default is most likely /home/<your_username>/PycharmProjects
    - set "Directory Name" to whatever you want, but for this we will be calling the "FwConfigApp" probably makes sense here

4. Configure pyCharm to use Python 3.4
  - once you clone the FwConfigApp repo pyCharm will most likely ask you go configure an interpreter for the project, but if not...
    - navigate to File > Settings > Project:FwCfgGen > Project Interpretter
    - set to "3.4.3 (/usr/bin/python3.4)
  
  Of course this assumes you have python 3.4 installed on your ubuntu machine, which if you are using a standard distribution should be the case. If this is a bad assumption on my part then you may have to double back real quick and install python 3.4...
    - sudo apt-get install python3.4

5. Install python dev packages for python 3.4
  The dev packages for python 3.4 are needed later on when we install SIPO. The instructions for installing the dev packages for python 3.4:
  - sudo apt-get install python3-dev

6. Install pyqt4 for python 3.4.
  Pyqt will need to have QT installed for the python. In this case since I am targetting python 3.4 I will need to install the pyqt4 packages for python 3.4.
  - sudo apt-get install python3-pyqt4

7. Install SIP
  Installing SIP is the first step toward getting the necessary python components installed for QT. Instructions can be found at http://pyqt.sourceforge.net/Docs/PyQt4/installation.html
  
  SIP is a package that generates python bindings to C and C++ libraries. This is required when we use QT as QT generates C libraries that that then need to be usable by python.
  
  - go to https://riverbankcomputing.com/software/sip/download and download the SIP source package for the LINUX OS
  - copy the downloaded tar file to /usr/src
  - open a terminal on your ubuntu machine
  - cd /usr/src/
  - sudo tar -xvf sip-4.19.tar.gz
    - Note - the name of your tar gz file may vary depending on latest available SIP version
  - cd /usr/src/sip-4.19
    - Note - the folder name may vary depending on latest available SIP version
  - sudo /usr/bin/python3.4 configure.py
    - this step will configure SIP specifically for python 3.4 (hence why the absolute path is provided)
  - sudo make
    - will build the necessary SIP libraries
  - sudo make install
    - will install the recently made SIP libraries

8. Install pyqt4.
  - sudo apt-get install python3-pyqt4  

    
    
 
