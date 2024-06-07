import socket
import sys

def scanHost(ip):

    #Ports to be scanned.
    ports = [22, 25, 53, 80, 443]

    print(f"[*] Starting TCP port scan on host {ip}")

    #Tries connecting to previously specified ports.
    for port in ports:
        try:

            #Create new socket
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #Try and connect to the port. Prints that the port is open if a connection is established.
            tcp.connect((ip, port))
            print(f"Port {port}: Open")
            tcp.close()

        except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()

        #Raise exception if a connection cannot be established to the port. 
        except socket.error:
            print(f"Port {port}: Closed")

    print(f"[+] TCP scan on host {ip} complete")


if __name__ == '__main__':

    #0.1s default timeout port response
    socket.setdefaulttimeout(0.1)

    #Accept IP address as a command line argument.
    if len(sys.argv) == 2:
        try:
            ip = socket.gethostbyname(sys.argv[1])
            scanHost(ip)
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    else:
        print("Invalid number of arguments. Only provide an IP address")

    # if len(sys.argv) >= 2 and len(sys.argv) < 5:
