# TCP client-server
## General info
This project is a simple UDP Client-Server program  divided in two parts: 

### Server  
allocate a socket and then repeatedly execute the following:
- wait for the next connection from a client
- receive lowercase sentence
- send uppercase sentence to client
- return to step 1


### Client  
allocate a socket, then:
- receive from stdin lowercase sentence
- send the sentence to the server
- receive from server the result and prints it
- close the program


**Written** in _python v3.8_ (support _v3.1+_)


## How to use?
If you want to use it like a server, just enter the server port number when you execute a program:  
`python3 "UDPClient.py" <your port number>`  
where the **port number** should be in range **(1024, 5000)**

If you want to use it like a client, just enter the server name and port number when you execute a program:  
`python3 "UDPClient.py" <your host name> <your port number>`  
where the **host name** in most cases is IP and the **port number** should be in range **(1024, 5000)**

Btw you can write  
`python3 "UDPClient.py" -help`  
to get instructions.

###[NOTE]:  
If you are using Linux you will need to make this file executable:
```
chmod +x "UDPClient.py"
```

###Example to use
The simplest way to check if program works correctly is written down here:  
1) Open the first terminal and write:  
   `python3 "UDPClient.py" 2048`  
to launch the server.  
2) Open the second terminal and write:  
   `python3 "UDPClient.py" 127.0.0.1 2048`  
to launch client.
3) Enter the sentence.
4) Get the same sentence with uppercase letters.