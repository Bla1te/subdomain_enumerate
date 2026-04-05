from domain.models import Subdomain

from typing import Callable

def get_subdomain_list(domain: str, words: list, get_ip: Callable) -> list:
    res = list()
    for word in words:
        full = word+'.'+domain
        new_subdomain = Subdomain(full, get_ip(full))
        res.append(new_subdomain)
    return res
