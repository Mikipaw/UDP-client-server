# -*- coding: utf-8 -*-
from socket import *
serverName = 'hostname'
serverPort = 12000

def udp_client():
    message = raw_input('Input lowercase sentence:')
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(message, (serverName, serverPort))
    modifiedMsg, serverAddr = clientSocket.recvfrom(2048)
    print (modifiedMsg)
    clientSocket.close()
