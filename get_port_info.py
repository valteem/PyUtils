import socket
import re
import sys
def check_server(address, port):
    # Create a TCP socket
    s = socket.socket()
    print("Attempting to connect to %s on port %s" % (address, port))
    try:
        s.connect((address, port))
        print("Connected to %s on port %s" % (address, port))
        print("Service running is %s " % socket.getservbyport(port))
        return True
    except socket.error as e:
        print("Connection to %s on port %s failed: %s" % (address, port, e))
        return False
    finally:
        s.close()

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("addr", help="IP address of the server")
    parser.add_argument("portnum", help="port number")
    args = parser.parse_args()
#    addr = '80.68.253.13'
#    port = 80
    check = check_server(args.addr, int(args.portnum))

if __name__ == '__main__':
    main()
