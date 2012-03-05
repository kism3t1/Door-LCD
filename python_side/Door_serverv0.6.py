# TCP server example
import socket
import serial
import time
import datetime
import sys
import argparse

the_Time = datetime.datetime.now()

if len(sys.argv) != 2:
        print ("[+] usage: ./Door_serverv0.5.py <HOST>")
        sys.exit(1)
PORT = int(sys.argv[1])
#HOST = " "
print ("The chosen port is ") + str(PORT)

ser = serial.Serial ('/dev/ttyACM0')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.bind(("", 5000))
server_socket.bind(("", PORT))
server_socket.listen(5)

print ("TCPServer Waiting for client on port ") + str(PORT)

while 1:
        client_socket, address = server_socket.accept()
        print "I got a connection from ", address
        while 1:
                data = client_socket.recv(512)
                if ( data == 'q' or data == 'Q'):
                        client_socket.close()
                        f = open('doorlog.ian', 'a')
                        f.write("Exiting Server @ " + (str(the_Time) + "/n"))
                        f.close
                        exit()
                        break;
                elif ( data == 'out'):
                        print "RECIEVED:" , data
                        ser.write("o")
                        f = open('doorlog.ian', 'a')
                        f.write("Out of Office @ " + (str(the_Time) + "/n"))
                        f.close
                elif ( data == 'in'):
                        print "RECIEVED:" , data
                        ser.write("i")
                        f = open('doorlog.ian', 'a')
                        f.write("In Office @ " + (str(the_Time) + "/n"))
                        f.close
                elif ( data == 'pub'):
                        print "RECIEVED:" , data
                        ser.write("p")
                        f = open('doorlog.ian', 'a')
                        f.write("Down the Pub @ " + (str(the_Time) + "/n"))
                        f.close
                elif ( data == 'yes'):
                        print "RECIEVED:" , data
                        ser.write("y")
                        f = open('doorlog.ian', 'a')
                        f.write("Come in! @ " + (str(the_Time) + "/n"))
                        f.close
                elif ( data == 'meeting'):
                        print "RECIEVED:" , data
                        ser.write("m")
                        f = open('doorlog.ian', 'a')
                        f.write("Sorry in a Meeting @ " + (str(the_Time) + "/n"))
                        f.close
                elif ( data == 'face'):
                        print "RECIEVED:" , data
                        ser.write("f")
                        f = open('doorlog.ian', 'a')
                        f.write("Displaying the FACE! @ " + (str(the_Time) + "/n"))
                        f.close
		elif (data == 'close'):
			print "RECIEVED:" , data
			client_socket.close()
			f = open('doorlog.ian', 'a')
			f.write("Retarting Connection... @ " + (str(the_Time) + "/n"))
			f.close
			print "Restarting connection:"
			#server_socket.bind(("", 5000))
			server_socket.listen(5)
			print "Door LCD: Waiting for Ian's PC on port 5000"

                else:
                        print("*")
