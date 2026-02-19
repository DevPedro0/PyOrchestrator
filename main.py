from project.config.config import Server

# Other Libs
import requests as r
import socket as s
import asyncio as asy
import pandas as pd
import uuid as u
import numpy as np
 
class Main():
    def __init__(self, url:str, responses = {}):
        self.url = url
        self.responses = responses
        self.json = {}
    
    def generate_id(self):
        return f"{len(self.json)}"
        
    async def connect(self) -> Server:
        if r.get(self.url).status_code != 200:
            self.STATUS = 404
            raise r.exceptions.ConnectionError(f"URL: {self.url} not Is Valid, imeplement your URL again...")
        self.STATUS = 200 # Defined Connection Sucess
        S = Server(self.url, self.responses)
        await S.on()
        return S
    
    def info(self, HOST = None, PORT = 80):
        address = s.getaddrinfo(
            HOST if HOST is not None else s.gethostname(),
            PORT, 
            proto = s.IPPROTO_TCP
        )
        # Descompactar
        ID = self.generate_id()
        self.json[ID] = {
            "ip": {},
            "mac": None,
            "type": None,
            "protocol": None,
            "stats": None
        }
        for i in address:
            family, type_, protocol, can, sockaddr = i
            mac = u.getnode()
            IP = sockaddr[0]
            MAC = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
            if (family == s.AF_INET) or (family == s.AF_INET6):
                k_string = f"{family}_INET_INFO_MAC_{IP.split(":")[-1]}" \
                    if family == s.AF_INET6 else f"{family}_INET_INFO_MAC_"
                json_ip = self.json[ID]["ip"]
                if k_string not in json_ip:
                    json_ip[k_string] = {}
                json_ip[k_string] = IP
                
            self.json[ID].update({
                "mac": MAC,
                "type": type_,
                "protocol": protocol,
                "stats": {}
            })
            
    def components(self, request):
        # Options
        ...
        
    def show_status(self, cols = []):
        ...
    
    def __call__(self, *args, **kwds):
        pass
    
    def __getattr__(self, it:str):
        d = None
        if (not callable(it)):
            self.__dict__[it] = d
    
if __name__ == "__main__":
    async def main():
        url = "https://www.google.com"
        Google = Main(url, {})
        Google.info()
        Google.info()
        Connect = await Google.connect()
    asy.run(main())