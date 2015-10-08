import sys
import socket

HOST = '127.0.0.1'
MAX_CONNECTIONS = 10
BUFLEN = 1024

def read_data_from_socket(socket):
	data = b''
	while True:
		data += socket.recv(BUFLEN)
		if b'\n' in data:
			break
	return data.decode('ascii')

def static_server(port):
	print('Starting a TCP server on http://{0}:{1}/\n'.format(HOST, port))
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((HOST, port))
	server_socket.listen(MAX_CONNECTIONS)

	while True:
		client_socket, client_addr = server_socket.accept()

		data = read_data_from_socket(client_socket)
		print(data)

		client_socket.send("received: " + data)
		client_socket.close()


def main():
	if len(sys.argv) != 2:
		print('Usage: {0} PORT'.format(sys.argv[0]))
		sys.exit(1)
	else:
		port = int(sys.argv[1])
		static_server(port)

if __name__ == '__main__':
	main()
