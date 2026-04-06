import argparse
import asyncio
from infrastructure.dns import get_ip
from infrastructure.load_list import load_subdamins_list
from usecases.func import get_subdomain_list, get_subdomain_list_crt
import json


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain')
    parser.add_argument('-crt', action='store_true')
    parser.add_argument('-json', action='store_true')
    parser.add_argument('-output')

    enter = parser.parse_args()


    if enter.crt:
        res = get_subdomain_list_crt(domain=enter.domain)
        res = [{'subdomain': i} for i in res]
        

        if enter.json:
            print(json.dumps(res,indent=1))
            if enter.output:
                with open(enter.output, "w") as f:
                    json.dump(res, f,indent=1)
        else:
            for i in res:
                print(i)
            if enter.output:
                with open(enter.output, "w") as f:
                    for i in res:
                        f.write(str(i.name)+'\n')


    else:
        words = load_subdamins_list('subdomains.txt')

        res = await get_subdomain_list(
            domain=enter.domain,
            words=words,
            get_ip=get_ip
        )

    

        if enter.json:
            res = [{'subdomain':i.name, 'ip': i.ip} for i in res]
            print(json.dumps(res, indent=2))
            if enter.output:
                with open(enter.output, "w") as f:
                    json.dump(res, f, indent=2)
        else:
            for i in res:
                print(i.name, i.ip)
            if enter.output:
                with open(enter.output, "w") as f:
                    for i in res:
                        f.write(str(i.name)+' '+str(i.ip)+'\n')


    

    return res

if __name__ == "__main__":
    asyncio.run(main())