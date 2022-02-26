
import socket
import sys
from datetime import datetime
import subprocess, platform
#โอ้คุณอยากเรียนรู้วิธีการเขียนมันหรอคุณสามารถสอบถามผมได้ที่เฟสบุ๊ค https://www.facebook.com/messages/t/104704474962816
#บางทีผมอาจช่วยคุณได้

def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls",
                         shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")

clear()
print("this script made by bell")
print("")
print("")
print("")
print("enter web URL")
print("example Target : example.com")
print("")
print("")
target = input("Target : ")
IP = socket.gethostbyname(str(target))
clear()
print("")
print("")
print("")
print("IP of target is " + str(IP))
print("")
print("scan port")
print("Please wait.....")

timestart = datetime.now()

try:
    for p in range(1, 9999):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((IP, p))
        if res == 0:
            if str(p) == "21":
                print("Connect in port " + str(p) + " FTP")
                print("")
            elif str(p) == "22":
                print("Connect in port " + str(p) + " SSH")
                print("")
            elif str(p) == "23":
                print("Connect in port " + str(p) + " telnet")
                print("")
            elif str(p) == "25":
                print("Connect in port " + str(p) + " smtp")
                print("")
            elif str(p) == "53":
                print("Connect in port " + str(p) + " dns")
                print("")
            elif str(p) == "80" or str(p) == "8080":
                print("Connect in port " + str(p) + " http")
                print("")
            elif str(p) == "110":
                print("Connect in port " + str(p) + " POP3")
                print("")
            elif str(p) == "135":
                print("Connect in port " + str(p) + " zero day")
                print("")
            elif str(p) == "143":
                print("Connect in port " + str(p) + " IMAP")
                print("")
            elif str(p) == "443":
                print("Connect in port " + str(p) + " https")
                print("")
            elif str(p) == "465" or str(p) == "587":
                print("Connect in port " + str(p) + " SMTP")
                print("")
            elif str(p) == "993":
                print("Connect in port " + str(p) + " IMAPS")
                print("")
            elif str(p) == "995":
                print("Connect in port " + str(p) + " POP3")
                print("")
            elif str(p) == "0":
                print("Connect in port " + str(p) + " 0")
                print("")
            elif str(p) == "5060":
                print("Connect in port " + str(p) + " SIP")
                print("")
            elif str(p) == "3306":
                print("Connect in port " + str(p) + " MySQL")
                print("")
            else:
                print("Connect in port " + str(p) + " unknow")
                print("")

        sock.close()

except Exception:
    print("error")
    sys.exit()

timestop = datetime.now()
time = timestop - timestart

print("Scan completed in " + str(time))