import re
import hashlib
import uuid
import base64

class Register():
    confirm_register = False
    def __init__(self, cpf, name, surname, email, password, confirm_password, *args, **kwargs):
        self.cpf = cpf
        self.name = name
        self.surname = surname
        self.e_mail = email
        self.password = password
        self.c_password = confirm_password
        self.a = args
        self.status_user = {}
    
    # Campus 
    def CPF(self):
        if len(self.cpf) != 9:
            raise Exception(f"The CPF value does not match reality; it has {len(self.cpf)} digits.")
        
        while True:
            n = self.cpf.__len__()
            start = 1 if n == 9 else 0
            char_save = 0
            if n != 11:
                for Index, i in enumerate(range(start, n+start)):
                    char = int(self.cpf[Index]) * i
                    char_save += char
                    if (Index+1 == n):
                        calc = char_save % 11
                        self.cpf += str(calc)
            else:
                return self.cpf
            
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
    
R = Register("152627416", "Pedro", "Henrique", "pedroexemplo@gmail.com", 1234, 1234)
R.CPF()