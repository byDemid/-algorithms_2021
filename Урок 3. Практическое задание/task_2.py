"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

from binascii import hexlify
from hashlib import pbkdf2_hmac


class UserData:
    def __init__(self, new_login, new_pass: str):
        self.login = new_login.lower()
        password_hash = pbkdf2_hmac(hash_name='sha256',
                                    password=new_pass.encode(),
                                    salt=self.login.encode(),
                                    iterations=100000)
        self._password_hash = hexlify(password_hash)

    def authorization(self, password):
        check_password = pbkdf2_hmac(hash_name='sha256',
                                     password=password.encode(),
                                     salt=self.login.encode(),
                                     iterations=100000)
        if self._password_hash == hexlify(check_password):
            print('Авторизация успешна')
        else:
            print('Авторизация не удалась')


login = input('Введите Логин: ')
password = input('Введите пароль: ')
user_1 = UserData(login, password)

auth_pass = password = input('Введите пароль: ')

user_1.authorization(auth_pass)

# Чисто разбирал задание поэтому копипас есть
