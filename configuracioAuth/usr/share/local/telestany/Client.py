import SOAPpy
import socket
import fcntl
import struct
import sys
import os
from SOAPpy import SOAPProxy
import platform
import array
import xml.sax
import xml.sax.handler

from xml.dom import minidom
from xml.dom.minidom import parseString

SIOCGIFCONF = 0x8912
MAXBYTES = 8096

def localifs():
    """
    Used to get a list of the up interfaces and associated IP addresses
    on this machine (linux only).

    Returns:
        List of interface tuples.  Each tuple consists of
        (interface name, interface IP)
    """
    global SIOCGIFCONF
    global MAXBYTES

    arch = platform.architecture()[0]

    # I really don't know what to call these right now
    var1 = -1
    var2 = -1
    if arch == '32bit':
        var1 = 32
        var2 = 32
    elif arch == '64bit':
        var1 = 16
        var2 = 40
    else:
        raise OSError("Unknown architecture: %s" % arch)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * MAXBYTES)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        sock.fileno(),
        SIOCGIFCONF,
        struct.pack('iL', MAXBYTES, names.buffer_info()[0])
        ))[0]

    namestr = names.tostring()
    return [(namestr[i:i+var1].split('\0', 1)[0], socket.inet_ntoa(namestr[i+20:i+24])) \
            for i in xrange(0, outbytes, var2)]

ifaces = localifs()
for iface in ifaces:
 	if ( iface[0] != 'lo'):
		eth = iface[0]

s = socket.socket()
config = minidom.parse(unicode("/usr/share/local/telestany",sys.getfilesystemencoding())+'/config.xml')
serverm = str(config.getElementsByTagName('GestorServer')[0].attributes["IP"].value)
if (len(sys.argv) > 1):
	if ( sys.argv[1] == "OBRO"):		
		s.connect((serverm,9999))
		d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', eth[:15]))[20:24])		
		host = socket.gethostname()
		s.send("OBRO|"+host)
		rebuc = s.recv(1024)
		print rebuc
		print "adios"
		s.close()
	if ( sys.argv[1] == "APAGO"):
		s.connect((serverm,9999))
		d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', eth[:15]))[20:24])
		host = socket.gethostname()
		s.send("APAGO|"+host)
		rebuc = s.recv(1024)
		print rebuc
		print "adios"
		s.close()
	if ( sys.argv[1] == "SURTO"):
		s.connect((serverm,9999))
		d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', eth[:15]))[20:24])
		host = socket.gethostname()
		s.send("SURTO|"+host+"|"+server.GetUserName(os.environ['USER']))
		rebuc = s.recv(1024)
		print rebuc
		print "adios"
		s.close()
