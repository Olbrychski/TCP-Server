# TCP-Server

This code creates a TCP server that can accept a maximum of N clients (where N is configurable). Clients are assigned ranks based on first-come-first-serve, with 0 being the highest rank. The server distributes commands among the clients and only allows clients with a lower rank to execute commands of higher rank clients. If a client disconnects, the server re-adjusts the ranks and promotes any client that needs to be promoted to prevent gaps in the ranks.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
![Visual Studio Code](https://img.shields.io/badge/-VSCode-000000?style=flat&logo=visual-studio-code&labelColor=007ACC)


###  Requirements
* Python 3

### 🛠 Installation
First check python version, Open a command prompt and run
 ```
$ python3 --version
 ```
To install python 3 for Linux run
 ```
$ sudo apt-get update
$ sudo apt-get install python3.6
 ```
### 🚀 Usage
Pull project to virtual environment (*[https://pypi.org/project/virtualenv/]()*). Then run.
```
$ git clone https://github.com/Olbrychski/TCP-Server
$ cd TCP-Server
$ virtualenv venv 
$ source venv/bin/activate 
$ python TCP_server.py  ```[IP ADDRESS]```
$ python client.py ```[SERVER IP ADDRESS]``` 
```

> NOTE: Replace  ```('HOST_IP_ADDRESS', PORT)``` with actual host IP address and port to be used before running TCP_server.py

### Configuration
The maximum number of clients that the server can accept is set by the variable N at the beginning of the code. This variable can be modified to change the maximum number of clients that the server can accept.

### Functionality
 * The server is initialized and binds to an IP address and port number.

 * When a client connects to the server, it assigns them a rank based on the first-come-first-serve principle and keeps track of the connected clients and their ranks using sets.

 * When a client sends a command to the server, it checks if the client has permission to execute the command based on their  rank. If a client has a lower rank, they can execute a command from a higher rank client.

 * If a client disconnects, the server re-adjusts the ranks and promotes any client that needs to be promoted to prevent gaps in the ranks.

 * The server continues to listen for new connections and handle the commands from the connected clients.

### OUTPUT
Output for 4 clients connected.
 ```
Server started listening on IP address: 192.168.1.100 and port: 6001
Client ('192.168.1.101', 8080) assigned rank 0
Client ('192.168.1.102', 8081) assigned rank 1
Client ('192.168.1.103', 8082) assigned rank 2
Client ('192.168.1.104', 8083) assigned rank 3

 ```

## License
[MIT](https://choosealicense.com/licenses/mit/)
