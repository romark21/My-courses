class User:
    pass

''' Объект (экземпляр класса) – это отдельный представитель класса, имеющий конкретное состояние и поведение,
 полностью определяемое классом'''

user = User() #создаём новый объект класса User

'''добавим несколько атрибутов (Python позволяет динамически привязывать новые атрибуты к объекту,
в конце концов это просто словарь)'''
user.user_name = 'Роман'
user.user_email = 'qwery@qwerty.qwe'
user.user_password = 'poiuyt'
print(user.__dict__)
print(user.user_name)
print(user.user_email) # Ниже выражения эквиваленто этому
print(user.__dict__['user_email']) # Выше выражения эквиваленто этому