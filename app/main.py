import argparse

from infrastructure.dns import get_ip
from infrastructure.load_list import load_subdamins_list
from usecases.func import get_subdomain_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain')

    enter = parser.parse_args()

    words = load_subdamins_list('subdomains.txt')

    res = get_subdomain_list(
        domain=enter.domain,
        words=words,
        get_ip=get_ip
    )

    for i in res:
        print(i.name, 'ip', i.ip)

    return res

if __name__ == "__main__":
    main()