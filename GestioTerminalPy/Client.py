import socket
import struct
import sys
import os

s = socket.socket()
s.connect(("172.17.14.48",9999))
host = socket.gethostname()
print host
#s.send("OBRO|"+host)
#s.send("USER|"+host+"|JESPINOSA")
#s.send("SURTO|"+host+"|JESPINOSA")
s.send("APAGO|"+host+"|JESPINOSA")
rebuc = s.recv(1024)
print rebuc
print "adios"
s.close()
