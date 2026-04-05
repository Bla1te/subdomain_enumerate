import socket

subdomains = ['www', 'api', 'mail', 'dev', 'shop', 'blog']

domain = 'yandex.ru'

for i in subdomains:
    full = i+'.'+domain
    try:
        ip = socket.gethostbyname(full)
    except:
        ip = None 
    print(full, '->', ip)