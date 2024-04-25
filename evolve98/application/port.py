import sys
import socket
from datetime import datetime
import errno
def scan():
 target = input("IP: ")

 print("-" * 50)
 print("Hedef: " + target)
 print("Başladığı tarih:" + str(datetime.now()))
 print("-" * 50)

 try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} açık".format(port))
        elif result == errno.ECONNREFUSED:
            print("Port {} kapalı".format(port))
        elif result == errno.EHOSTUNREACH:
            print("Port {} filtrelenmiş".format(port))
        s.close()
        
 except KeyboardInterrupt:
    sys.exit()
 except socket.gaierror:
    print("IP bulunamadı")
    sys.exit()
 except socket.error:
    print("Server bulunamadı")
    sys.exit()
