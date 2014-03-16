import socket

PORT = 23456

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind((socket.gethostname(), PORT))
s_sock.listen(5)

print "[+] Listening on port " + str(PORT) + "."

(c_sock, addr) = s_sock.accept()
print "[+] Accepted connection from: " + str(addr)+ "."
#ct = client_thread(c_

while 1:
    msg = c_sock.recv(0x200)
	
	if msg == '':
		break
	
    print "[+] Client sent: " + msg

s_sock.close()
