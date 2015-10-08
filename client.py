import sys
import socket

HOST = '127.0.0.1'

def send_data(port):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((HOST, port))
	client_socket.send("{0}\n".format("data"))
	client_socket.send("{0}\n".format("data1"))
	data = client_socket.recv(1024)
	print data
	

def main():
	if len(sys.argv) != 2:
		print('Usage: {0} PORT'.format(sys.argv[0]))
		sys.exit(1)
	else:
		port = int(sys.argv[1])
		send_data(port)

if __name__ == '__main__':
	main()
