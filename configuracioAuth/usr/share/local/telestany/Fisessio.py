import SOAPpy
import time
import os
import socket
import fcntl
import struct
import sys
from datetime import datetime,date, timedelta
from SOAPpy import SOAPProxy
from time import gmtime, strftime

server = SOAPProxy('http://213.151.114.85:8082/')
idUser = server.GetUser(os.environ['USER'])
server.AddLogLloc(idUser,strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'SURT','Telestany')
