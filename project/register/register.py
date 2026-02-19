import re
import hashlib
import uuid
import base64

class Register():
    confirm_register = False
    def __init__(self, cpf:str, name, surname, email, password, confirm_password, *args, **kwargs):
        self.cpf = cpf
        self.name = name
        self.surname = surname
        self.e_mail = email
        self.password = password
        self.c_password = confirm_password
        self.a = args
        self.status_user = {}
        self.validate()
    
    def validate(self):
       ...
    
    # Campus 
    def CPF(self):
        while True:
            # Construct and Validate CPF Number
            n = self.cpf.__len__()
            
            start = 1 if n == 9 else 0
            char_save = 0
            if n != 11:
                for Index, i in enumerate(range(start, n+start)):
                    char = int(self.cpf[Index]) * i
                    char_save += char
                    if (Index+1 == n):
                        calc = char_save % 11
                        calc = 0 if calc >= 10 else calc
                        self.cpf += str(calc)
            else:
                break
            
    def EMAIL(self):
        return self.email
        
    def PASSWORD(self):
        key = 0
        return key
    
    @property
    def _NAME(self):
        f"{self.name} - {self.surname}"
    
    @property
    def _CPF(self):
        return self.CPF()
    
    @property
    def _EMAIL(self):
        return self.EMAIL()
    
    def __getattr__(self, item):
        if (not self.confirm_register):
            # Block User or Redirect User for Page Register
            ...
    
R = Register("16899535120", "Pedro", "Henrique", "pedroexemplo@gmail.com", 1234, 1234)
print(R._CPF)