import socket

Host="localhost"
Port=5000

socket_dict={}
data=' '
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,Port))
s.listen(1)
print 'ready to accept request'
name="GOOOGLY_DNS"
while 1:
    conn,addr=s.accept();
    data=conn.recv(1024)
    if data.split()[0] == "client":
        x=socket_dict.get(data.split()[1])
        if x is not None :
            req_addr=x
        else:
            req_addr="not available"
        conn.send(req_addr)
    else:
        socket_dict[data.split()[2]]=data.split()[0]+" "+data.split()[1]
        print data," server has been added successfull"
        print "IP : ",data.split()[0]
        print "PORT : ",data.split()[1]
        conn.send(name)

s.close()
