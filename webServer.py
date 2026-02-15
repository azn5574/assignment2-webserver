# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      #opens the client requested file. 
      f = open(filename[1:], "rb")
      
      

      #Fill in start 
      outputdata = b"HTTP/1.1 200 OK\r\n"
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"Server: MyWebServer\r\n"
      outputdata += b"Connection: close\r\n"
      outputdata += b"\r\n"
      #Fill in end
               
      for i in f:
        outputdata += i
        
      # Fill in start
      connectionSocket.send(outputdata)
      # Fill in end
        
      connectionSocket.close()
      
    except Exception as e:
      #Fill in start
      output = b"HTTP/1.1 404 Not Found\r\n"
      output += b"Content-Type: text/html; charset=UTF-8\r\n"
      output += b"Server: MyWebServer\r\n"
      output += b"Connection: close\r\n"
      output += b"\r\n"
      output += b"<html><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.send(output)
      #Fill in end

      #Fill in start
      connectionSocket.close()
      #Fill in end

  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING
  #serverSocket.close()
  #sys.exit()

if __name__ == "__main__":
  webServer(13331)