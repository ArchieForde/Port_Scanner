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


def scan_the_ports(host, start_port, end_port):
    print(f"Scanning ports {start_port} to {end_port} on {host}.")
    for port in range (start_port, end_port + 1):
        scan_the_port(host, port)

if __name__ == "__main__":
    target_host = input("Enter the IP address or hostname of the target: ")
    start_port = int(input("Enter the starting Port number: "))
    end_port = int(input("Enter the ending Port number: "))

    scan_the_ports(target_host, start_port, end_port)
