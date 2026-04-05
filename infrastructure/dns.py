import socket


def get_ip(subdomain: str) -> str | None:
    try:
        ip = socket.gethostbyname(subdomain)
    except:
        ip = None 
    return ip