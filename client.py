import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.29.225',3389))
print("Connection Successful")
msg = s.recv(1024)
print(msg.decode("utf-8"))
while True:
    temp=input("Enter Tempearature in Fahrenheit or 'NO' to Stop\n")
    if(temp=='NO'):
        break
    s.send(bytes(temp,'utf-8'))
    tempf=s.recv(4096)
    tempf.decode('utf-8')
    tempf=float(tempf)
    print("The Temperature in Fahrenheit is")
    print('%.2f'%tempf)
s.close()
    

