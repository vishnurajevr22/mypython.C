import socket 
s = socket.socket
print("connecting to server..")
s.connect(('127.0.0.1',20564))
print("connection waiting for message...")
data=s.recv(1024)
print("received:",data.decode())
s.close()
input("press enter to exit...")