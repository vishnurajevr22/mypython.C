import socket
s=socket.socket()
s.bind(('127.0.0.1',20564))
s.listen(1)
print("socket is listening...")

c,addr=s.accept()
print("got a connection from",addr)
c.send(b"thank you for connecting")
c.close()
s.close()
