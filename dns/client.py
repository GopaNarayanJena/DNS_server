import socket

def calserver(addr,data):
    hostcal=addr.split()[0]
    portcal=int(addr.split()[1])
    scal=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    scal.connect((hostcal,portcal))
    scal.send(data)
    ans=scal.recv(1024)
    print "ans : ",ans
    scal.close()

Host="localhost"
Port=5000

data=' '
cache_dict={}
print "NOTE:"
print "=================================="
print "to addition : add 1 2"
print "to subtraction : sub 7 2"
print "to multiplication : multiply 1 2"
print "to divide : divide 4 2"
print "to exit : exit"
print "=================================="
while data!='exit':
    print "enter command :"
    data=raw_input()
    data=data.strip()
    cmd=data.split()[0];
    cache=cache_dict.get(cmd)
    if cache is None:
        sdns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sdns.connect((Host,Port))
        sdns.send("client "+cmd)
        response=sdns.recv(1024)
        if response == "not available":
            print "404 SERVER NOT FOUND"
        else:
            cache_dict[cmd]=response
            calserver(cache_dict[cmd],data)
    else:
        calserver(cache_dict[cmd],data)
        sdns.close()
