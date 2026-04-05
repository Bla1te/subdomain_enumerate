import socket


def check(subdomain: str):
    try:
        ip = socket.gethostbyname(subdomain)
    except:
        ip = None 
    return ip

with open('subdomains.txt') as f:   
    subdomains = [i[:len(i)-1] for i in f ]

domain = 'yandex.ru'

for i in subdomains:
    full = i+'.'+domain
    
    print(full, '->', check(full))