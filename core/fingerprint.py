import socket

def get_service_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n" if port == 80 else b"\r\n")
        banner = s.recv(1024).decode(errors='ignore').strip()
        s.close()
        return banner if banner else "No Banner Found"
    except:
        return "Service Unreachable"