from domain.models import Subdomain
import asyncio
from typing import Callable




async def get_subdomain_list(domain: str, words: list, get_ip: Callable) -> list:
    res = list()
    full_names = [word+'.'+domain for word in words]

    ips = await asyncio.gather(
        *(asyncio.to_thread(get_ip, full) for full in full_names)
    )
    for i in range(len(full_names)):
        
        new_subdomain = Subdomain(full_names[i], ips[i])
        res.append(new_subdomain)

    return res
