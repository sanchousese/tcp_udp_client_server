import socket
import sys

HOST = "127.0.0.1"

def static_server(port):
	print('Starting a UDP server on http://{0}:{1}/\n'.format(HOST, port))
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_socket.bind((HOST, port))

	while True:
		data, client_addr = server_socket.recvfrom(1024) # buffer size is 1024	
		print('Connected from: {0}'.format(client_addr))
		print "sended: ", data
	

def main():
	if len(sys.argv) != 2:
		print('Usage: {0} PORT'.format(sys.argv[0]))
		sys.exit(1)
	else:
		port = int(sys.argv[1])
		static_server(port)

if __name__ == '__main__':
	main()
