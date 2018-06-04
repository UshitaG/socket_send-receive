#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#will atleast run once
k='y'
j=("127.0.0.1",9999)

#to bind the server
s.bind(j)			

#if user wants to enter again
while k[0]=='y':
	a=s.recvfrom(100)
	print "Message is: "+a[0]
	s.sendto("Type again?(y/n)",a[1])	#ask user if he wants to send again
	k=s.recvfrom(100)
