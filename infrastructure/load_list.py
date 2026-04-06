

def load_subdamins_list(path: str) -> list:
    subdomains = list()
    with open(path) as f:   
        for i in f:
            if i[len(i)-1] == '\n':
                subdomains.append(i[:len(i)-1])
            else:
                subdomains.append(i)

    return subdomains