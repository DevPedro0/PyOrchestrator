import re

class Register():
    def __init__(self, cpf, name, surname, email, password, confirm_password, *args, **kwargs):
        self.url = kwargs.get("url", "")
        self.cpf = cpf
        self.name = name
        self.surname = surname
        self.e_mail = email
        self.password = password
        self.c_password = confirm_password
        self.a = args
    
    def register(self):
        ...