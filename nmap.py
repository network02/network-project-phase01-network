import socket

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5) # Setting timeout to 5 seconds
    try:
        s.connect((host,port))
        return True
    except:
        return False
    finally:
        s.close()

def check_port_range(host, s_port, e_port):
    for port in range(s_port, e_port):
        if is_port_open(host, port):
            print(f"Port {port} is open.")
            try:
                serviceName = socket.getservbyport(port, "tcp")
                print(f"TCP service: {serviceName}")
                serviceName = socket.getservbyport(port, "udp")
                print(f"UDP service: {serviceName}")
            except Exception as error:
                print(f"service port:{error}")
        else:
            print(f"Port {port} is close.")

def is_host_online(host):
    PORTS = [20, 21, 22, 25, 53, 80, 123, 443]
    is_online = False
    for port in PORTS:
        if is_port_open(host, port):
            print(f"Port {port} is open, so host is online!")
            is_online = True
            break

    if not is_online:
        print("Specified ports were all close, so host is not online!")

def main():
    mode = input("Enter 1 to check host availability or 2 to check a range of ports: ")
    if mode == "1":
        host = input("Enter host: ")
        is_host_online(host)
    elif mode == "2":
        host = input("Enter host: ")
        min_port = int(input("Enter start range: "))
        max_port = int(input("Enter end range: "))
        check_port_range(host, min_port, max_port)
    else:
        print("Input was not valid.")
        
        
if __name__ == '__main__':
    main()