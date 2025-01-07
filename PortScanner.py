import socket

def scan_the_port(host, port):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(1)
        result = soc.connect_ex((host, port)) 

        if result == 0:
            print(f"The Port {port} on {host} is OPEN...")
        else:
            print(f"The Port {port} on {host} is CLOSED...")

        soc.close

    except socket.error:
        print(f" An Error was detected when connecting to {host} on port {port}.")