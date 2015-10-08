import socket
import sys

HOST = "127.0.0.1"

def send_data(port):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client_socket.sendto("Message", (HOST, port))

def main():
	if len(sys.argv) != 2:
		print('Usage: {0} PORT'.format(sys.argv[0]))
		sys.exit(1)
	else:
		port = int(sys.argv[1])
		send_data(port)

if __name__ == '__main__':
	main()
