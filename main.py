from project.config.config import Server

# Other Libs
import requests as r
import os
import platform
import socket as s
import asyncio as asy
 
class Main():
    def __init__(self, url:str, responses = {}):
        self.url = url
        self.responses = responses
        self.json = {}
        
    def add(self, key:str, value, *args, **kwargs) -> None:
        self.json[key] = value
    
    async def connect(self) -> Server:
        if r.get(self.url).status_code != 200:
            self.STATUS = 404
            raise r.exceptions.ConnectionError(f"URL: {self.url} not Is Valid, imeplement your URL again...")
        self.STATUS = 200 # Defined Connection Sucess
        S = Server(self.url, self.responses)
        await S.on()
        return S
    
    def info(self, HOST, PORT = 80):
        parcial_list = []
        address = s.getaddrinfo(
            s.gethostname(),
            PORT, 
            proto = s.IPPROTO_TCP
        )
        # Descompactar
        for i in address:
            family, type_, protocol, can, sockaddr = i
            MAC = sockaddr[0]
            if (family == s.AF_INET) or (family == s.AF_INET6):
                k_string = f"{family}_INET_INFO_MAC_{MAC.split(":")[-1]}" \
                    if family == s.AF_INET6 else f"{family}_INET_INFO_MAC_"
                    
                self.add(k_string, [[MAC, PORT, HOST], protocol])
                
    def components(self, request):
        # Options
        ...
    
    def __call__(self, *args, **kwds):
        pass
    
    @property
    def _json(self):
        return self.json
        
if __name__ == "__main__":
    try:
        url = "https://www.google.com"
        Google = Main(url, {})
        Google.info(1234)
        print(Google._json)
        
    except r.exceptions.ConnectionError as E:
        raise r.exceptions.ConnectionError(f"URL: {url} not Is Valid, imeplement your URL again...")