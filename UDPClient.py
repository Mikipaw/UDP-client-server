# -*- coding: utf-8 -*-
from socket import *
import sys

#serverName = 'hostname'
#serverPort = 12000

BUFFER_SIZE      = 2048
PORT_LOWER_BOUND = 1024
PORT_UPPER_BOUND = 5000


def udp_client(serverName, serverPort):
    message = raw_input('Input lowercase sentence:')
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(message, (serverName, serverPort))
    modifiedMsg, serverAddr = clientSocket.recvfrom(BUFFER_SIZE)
    print (modifiedMsg)
    clientSocket.close()


# The function checks user-entered parameters for client work
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
        message, clientAddr = serverSocket.recvfrom(BUFFER_SIZE)
        modifiedMsg = message.upper()
        serverSocket.sendto(modifiedMsg, clientAddr)


# The function checks user-entered parameters for server work
def check_server_params(serverPort):
    if int(sys.argv[1]) > 5000 or int (sys.argv[1]) < 1024:
        print("Port number invalid. Port number should be in range (1024, 5000).")
        return False
    return True        


def PrintInformation():
    print("This program maintains working like a server with UDP socket and like a client.")
    print("If you want to use the program like a server, just enter the server port when you run a program. For example, \"python UDPClient 2048\"")
    print("If you want to use the program like a client, just enter the server name and port number when you run a program. For example, \"python UDPClient hostname 2048\"")
    print("Port number must be in range (1024, 5000) to correct execution")
    return
        

if __name__ == '__main__':
    if len (sys.argv) == 3:
        type = check_client_params(sys.argv[1], sys.argv[2]) #checks server name and port number
        if type:
            udp_client(sys.argv[1], int(sys.argv[2]))
        else:
            print("Invalid input")
            print("Please, enter \"python UDPClient -help\" to get instructions")

    elif len (sys.argv) == 2: #checks port number
        type = check_server_params(sys.argv[1])
        if type:
            udp_server(int(sys.argv[1]))
        elif sys.argv[1] == "-help":
            PrintInformation()
        else:
            print("Invalid input")
            print("Please, enter \"python UDPClient -help\" to get instructions")

    else:
        print("Invalid input! The programm expects 1 or 2 params, but {} were given").format(len(sys.argv) - 1)
        print("Please, enter \"python UDPClient -help\" to get instructions")