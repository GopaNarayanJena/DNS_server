import socket
import sys

Hostdns="localhost"
Portdns=5000

Host="localhost"
Port=5004

sdns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sdns.connect((Hostdns,Portdns))
addr=Host+" "+str(Port)+" divide"
sdns.send(addr)
data=sdns.recv(1024)
if data == "GOOOGLY_DNS":
    print "add server is registered in  GOOOGLY_DNS"
sdns.close()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,Port))
s.listen(1)
while 1:
    conn,addr=s.accept()
    data=conn.recv(1024)
    a=data.split()[1]
    b=data.split()[2]
    conn.send(str(float(a)/float(b)))
s.close()
