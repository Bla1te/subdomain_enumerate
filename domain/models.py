from dataclasses import dataclass

@dataclass
class Subdomain():
    name: str
    ip: str | None

    def is_valid(self):
        return self.ip != None
    
