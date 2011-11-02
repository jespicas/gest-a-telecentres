import SOAPpy
import time
import os
from datetime import datetime,date, timedelta
from SOAPpy import SOAPProxy
from time import gmtime, strftime

server = SOAPProxy('http://213.151.114.85:8082/')
idUser = server.GetUser(os.environ['USER'])
server.AddLog(idUser,strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'SURT')
