# -*- coding: utf-8 -*-
from socket import *
#serverName = 'hostname'
#serverPort = 12000
bufferSize = 2048

def udp_client(serverName, serverPort):
    message = raw_input('Input lowercase sentence:')
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(message, (serverName, serverPort))
    modifiedMsg, serverAddr = clientSocket.recvfrom(bufferSize)
    print (modifiedMsg)
    clientSocket.close()

def check_client_params(serverName, portNumber):
    if int(sys.argv[2]) > 5000 or int (sys.argv[2]) < 1024:
        print("Port number invalid. Port number should be in range (1024, 5000).")
        return False
    try:
        socket.gethostbyname(sys.argv[1])
    except socket.error:
        print("Invalid host name. Exiting.")
        return False
    return True

def udp_server(serverPort):
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print ("The server is ready to receive")
    while True:
        message, clientAddr = serverSocket.recvfrom(bufferSize)
        modifiedMsg = message.upper()
        serverSocket.sendto(modifiedMsg, clientAddr)
        
def check_server_params(serverPort):
    if int(sys.argv[1]) > 5000 or int (sys.argv[2]) < 1024:
        print("Port number invalid. Port number should be in range (1024, 5000).")
        return False
    return True        
        
if __name__ == '__main__':
    if len (sys.argv) == 3:
        type = check_client_params(sys.argv[1], sys.argv[2]) #checks server name and port number
        if type:
            udp_client(argv[1], int(argv[2]))
        else:
            print("Invalid input")
    elif len (sys.argv == 2): #checks port number
        type = check_server_params()
        if type:
            udp_server(int(argv[1]))
        else:
            print("Invalid input")
    else:
        print ("Invalid input! The programm expects 1 or 2 params, but {} were given").format(len(sys.argv) - 1)