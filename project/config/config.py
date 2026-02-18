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
        
    def error(self, status = 404):
        # Error Server Load
        if not self.load:
            msg_error = f"[ERROR - {status}] It is not possible to run tasks on the server when it is turned off.\nFor educational purposes, turn on the server."
            raise Exception(msg_error)
    # Connect
    async def connect(self, IP, address_MAC, identified, user_Agent, stats:dict, *args, **kwargs):
        self.error()
        print("Init Connection...")
        # Defined Params Connect
        self.json["connect"] = {
            "ip": IP,
            "mac": address_MAC,
            "stats": stats
        }
        return self.json["connect"]
    
    # Methdos Controls User    
    async def response(self, status:int = 404):
        self.error(status)           
        return self.json.get("response", status)
    
    async def lock_connection(self, defined_status:int = 404, list_user:str|list = [], \
                         time_block = 30, permanent_Lock = False):
        self.error()
    
    # Modes
    async def on(self, msg = "Server On..."):
        await asy.sleep(2)
        if self.load:
            print("[INFO]: Server Is Connected!!")
            self.show_status()
            return
        elif msg == "":
            msg = "Server On..."
            
        print(f"{msg}")
        self.load = True
        
    async def off(self, msg = "Server Off"):
        await asy.sleep(1)
        if self.load:
            print("Disconected Server...")
            self.show_status()
        else:
            raise Exception("Server not Init...")
        
        self.load = False
        print(f"{msg}")
    
    # Propertys
    @property
    def _url(self) -> str:
        return self.url
    
    @_url.setter
    def _url(self, value:str) -> str:
        if not isinstance(value, str):
            raise TypeError("Value not String!!")
        self.url = value
        return self.url
    
    # Show Status
    def show_status(self):
        s = "#"
        print(f"\n{s*20} ===== STATUS SERVER ===== {s*20}")
        print(f"Url: {self.url}")
        print(f"Responses: {self.responses}")
        print(f"Stats Connection: {self.json.get('connect', [])}")
        print(f"{s*20} ===== STATUS SERVER ===== {s*20}\n")
        
        return
    
    # By Init
    def __getattr__(self, it:str):
        d = None
        if (not callable(it)):
            self.__dict__[it] = d
    
    # By Class
    @classmethod
    def __getattr__(cls, it):
        d = None
        if (not callable(it)):
            cls.__dict__[it] = d