# Port Scanner

## Objective

The Port Scanner project aimed to develop a tool that scans a range of ports on a target system to identify which ports are open or closed. The goal was to learn how network communication works, specifically regarding TCP/IP protocols, while practicing socket programming in Python. This project allowed for the exploration of fundamental cybersecurity concepts such as scanning, network vulnerability assessment, and the identification of services running on specific ports.

### Skills Learned

- Understanding of networking fundamentals like IP addresses, ports, and socket communication.
- Practical experience with socket programming in Python.
- Familiarity with the concept of port scanning and its applications in penetration testing.
- Ability to assess network security by identifying open and closed ports.
- Basic knowledge of how attackers use port scanners in vulnerability assessment and attack preparation.

### Tools Used

- Python programming language, specifically the socket library for network communication.
- Basic terminal or command-line interface (CLI) for executing the port scanner.

## Steps

1. Setting up the environment: I created a Python script using the socket library to establish TCP connections to specified ports on a target host.

2. Scanning Ports: The script allows the user to input the target system's IP address or hostname and scan a range of ports. The program then attempts to connect to each port and determines whether it's open or closed.

3. Displaying Results: The program outputs whether a port is open or closed, providing insight into the target system’s exposed services.
