import flask

from flask import render_template

class User:
    """user info"""


    def __init__(self,
    login:str,
    email:str,
    password:int,
    first_name:str,
    last_name:str,
    )-> None:
        self.login = login
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create(
        login:str,
        email:str,
        password:int,
        password2:int,
        first_name:str,
        last_name:str, 
        users:list['User']
    )->'User':
        if password !=password2:
            raise ValueError(
                "Пароли не совподают"
            )

        user: User = User(
            login = login,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name
            )
        if user.is_valid(users):
            return user
        else:
            raise ValueError(
                "Error"
            )

   
    def is_valid(self, users:list['User']) -> bool:
        user: User
        domain_pattern:tuple = (
            'net','com','kz','ru','org'
        )
        email_parts:list[str] = self.email.split('@')
        email_parts_by_point:list[str] = self.email.split('.')

        if (
            len(email_parts) !=2
        ) or (
            len(email_parts[0]) <=2
        ) or (
           len(email_parts_by_point) !=2
        ) or (
            not email_parts_by_point[1] in domain_pattern
        ):
            raise ValueError(
                'Не верный email!'
            )
        pass_simbol:tuple = (
            '@','/','%','&','*','!','#','$','(',')','_','-','=','^'
        )
        for i in self.password:
            for j in pass_simbol:
                    if i == j:
                        raise ValueError(
                        'В пароле содержатся запрещенные символы'
                        )
        for user in users:
            if user.login == self.login:
                return False
        if len(self.password) < 6:
            return False
        if len(self.first_name) >= 20:
            raise ValueError(
                        'Слишком длинное имя'
                        )
        if len(self.last_name) >= 20:
            raise ValueError(
                        'Слишком длинная Фамилия'
                        )
        return True
        