import asyncio as asy

class Server():
    def __init__(self, url, responses = None, *args, **kwargs):
        ''''
        implement Status Logging
        '''
        self.json = {}
        self.url = url
        self.responses = responses
        self.heating = kwargs.get("heats")
        self.load = False
        
    async def error(self, status = 404):
        # Error Server Load
        if not self.load:
            msg_error = f"[ERROR - {status}] It is not possible to run tasks on the server when it is turned off.\nFor educational purposes, turn on the server."
            raise Exception(msg_error)
    
    async def connect(self, IP, address_MAC, identified, user_Agent, stats:dict, *args, **kwargs):
        await self.error()
        print("Init Connection...")
        # Defined Params Connect
        self.json["connect"] = {
            "IP": IP,
            "MAC": address_MAC,
            "Id": identified,
            "Agents_User": user_Agent,
            "Stats": stats
        }
        return self.json["connect"]
        
    async def response(self, status:int = 404):
        await self.error(status)           
        return self.json.get("response", status)
        
    async def lock_connection(self, defined_status:int = 404, list_user:str|list = [], \
                         time_block = 30, permanent_Lock = False):
        await self.error()
    
    async def on(self, msg = "Server On..."):
        await asy.sleep(2)
        if self.load:
            print("[INFO]: Server Is Connected!!")
            return
        print(f"{msg}")
        self.load = True
        
    async def off(self, msg = "Server Off"):
        await asy.sleep(1)
        if self.load:
            print("Disconected Server...")
        else:
            raise Exception("Server not Init...")
        self.load = False
        print(f"{msg}")
    
    @property
    def _url(self) -> str:
        return self.url
    
    @_url.setter
    def _url(self, value:str) -> str:
        if not isinstance(value, str):
            raise TypeError("Value not String!!")
        self.url = value
        return self.url
    
    @property
    def _server(self):
        s = "#"
        print(f"{s*20} ===== STATUS SERVER ===== {s*20}")
        print(f"Url: {self.url}")
        print(f"Responses: {self.responses}")
        print(f"Stats Connection: {self.json.get("connect", [])}")
        print(f"{s*20} ===== STATUS SERVER ===== {s*20}")

