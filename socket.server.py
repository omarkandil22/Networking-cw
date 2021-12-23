
import socket 
from uuid import getnode as get_mac

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431    # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        
     
        while True:
            data = conn.recv(1024)
            my_mac = ':'.join(("%012X" % get_mac())[
                              i:i+2] for i in range(0, 12, 2))
            
            print('Recieved from the client: ',data)
            print("sender IP is :",s.getsockname()[0])
            print("sender PORT is :",s.getsockname()[1])
            print("My mac address is: ", my_mac)
                            
            
            if not data:
                break
            conn.sendall(data)


