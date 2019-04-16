import socket
import threading
sever=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sever.bind(('0.0.0.0',8001))
sever.listen()
def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        if data.decode("utf8") == 1:
            break
        send_data = input()
        sock.send("Sever: {}".format(send_data).encode("utf8"))
    sever.close()
    sock.close()
while True:
    sock, addr = sever.accept()
    Client_threading=threading.Thread(target=handle_sock,args=(sock,addr))
    Client_threading.start()

# sever.close()
# sock.close()