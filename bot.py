'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + ''' 

             ███████╗███╗   ███╗ █████╗ ██╗██╗     
             ██╔════╝████╗ ████║██╔══██╗██║██║     
             █████╗  ██╔████╔██║███████║██║██║     
             ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     
             ███████╗██║ ╚═╝ ██║██║  ██║██║███████
             ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝  ''')
