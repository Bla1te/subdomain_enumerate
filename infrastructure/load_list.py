

def load_subdamins_list(path: str) -> list:
    with open('subdomains.txt') as f:   
        subdomains = [i[:len(i)-1] for i in f ]
    return subdomains