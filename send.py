#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
d='y'
b=("127.0.0.1",9999)
while d=='y':
	msg=raw_input("Enter your message:")
	s.sendto(msg,b)			#send message to server
	p=s.recvfrom(100)	 	#receive from server
	print p[0]				
	d=raw_input()		#Input whether user wants to send again
	s.sendto(d,p[1])


