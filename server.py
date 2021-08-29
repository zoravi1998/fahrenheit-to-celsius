import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',3389))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the Celsius to Farhenheit Conversion Service","utf-8"))
    tf=0
    while True:
        data=clientsocket.recv(4096)
        if not data: break
        data.decode('utf-8')
        print (f'Data recieved Successfully {data}')
        tempc=float(data)
        tf=(tempc*1.8)+32
        tf=str(tf)
        tf=bytes(tf,'utf-8')
        clientsocket.send(tf)
    clientsocket.close()
    print('Client Disconnected')