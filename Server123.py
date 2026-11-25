from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
app.config['RESTFUL_JSON'] = {'ensure_ascii': False}
api = Api(app)




tableUsers = [
    {
        'id': 1, 
        'login': 'ivanov',
        'password': '123',
        'name': 'Иван',
        'surname': 'Иванов',
        'age':'34',
        'birthdate': '12.12.1890'
    },
    {
        'id': 2, 
        'login': 'ivanov1',
        'password': '123',
        'name': 'Иван',
        'surname': 'Иванов',
        'age':'34',
        'birthdate': '12.12.1890'
    }
]

class Login(Resource): #вход по логину бывалых
    def post(self):
        
        method = request.method
        
        if method == 'POST':
        
            data = request.get_json()
        
        login = data.get('login')
        password = data.get('password')
         
        if not login or not password:
            return {
                "status": "FAILED",
                "error": "Поля 'login' и 'password' обязательны для заполнения"
            }
        
        for user in tableUsers:
            if user['login'] == login and user['password'] == password:
                return {
                    "status": "OK",
                    "error": ""
                }
                
        return {
            "status": "FAILED",
            "error": "Пользователь и пароль не найдены"      
        }

class Users(Resource): 
    def get(self): # вывод всех данных пользоваталей
        return tableUsers  
        
        
        
    def put(self): # регистрация данных НОВЫХ пользователей 
        method = request.method
                
        if method == 'PUT':
            data = request.get_json()
        
        login = data.get('login') # достаем данные чтоб потом что то обратно отправить
        password = data.get('password')
        name = data.get('name')
        surname = data.get('surname')
        age = data.get('age')
        birthdate = data.get('birthdate')
        
        if not name or not surname or not age or not login or not password or not birthdate:
            return{
                    "status": "FAILED",
                    "error":"Извините, вы что то не заполнили"
                }
        
        
        for user in tableUsers:
            if user['login'] == login:
                return{
                        "status": "FAILED",
                        "error":"Пользователь с таким логином уже существует"
                    },
           
           
        new_id = max([user['id'] for user in tableUsers]) + 1
                 
        new_user = {
            'id': new_id,
            'login': login,
            'password': password,
            'name': name,
            'surname': surname,
            'age': age,
            'birthdate': birthdate
            
        }
            
        tableUsers.append(new_user)
        return {
                "status": "OK",
                "error":""
            }
    
    def patch(self): #смена данных 
        
        data = request.get_json() # форматирует прилегающий от клиента запрос Json в словарь
        
        if not data:
            return {
                    "status":"FAILED",
                    "error":"В теле запроса должен быть Json"
                }
        
        foundUser = None
        
        searchId = data.get("id")
        
        if not searchId:
            return {
                "status":"FAILED",
                "error":"Id не указан"
            }
        
        for user in tableUsers: 
            if user['id'] == searchId:
                foundUser = user
                break
            
        
        if not foundUser:
            return {
                "status":"FAILED",
                "error":"Не нашлось пользователя с таким логином"
            }
            
            
        if "name" in data: # проверяем есть ли ключ в данных от data
            foundUser["name"] = data["name"] #если нет, то мы ничего не меняем, а если есть то меняем на результат found_user
        if "surname" in data:
            foundUser["surname"] = data["surname"]
        if "age" in data:
            foundUser["age"] = data["age"]
        if "password" in data:
            foundUser["password"] = data["password"]
        if "birthdate" in data:
            foundUser["birthdate"] = data["birthdate"]
        
        return{
            "status":"OK",
            "error":""
        }
        
    def delete(self):
        data = request.get_json() # форматирует прилегающий от клиента запрос Json в словарь
                
        if not data:
            return {
                    "status":"FAILED",
                    "error":"В теле запроса должен быть Json"
                }
        
        foundUser = None
        
        searchId = data.get("id")
        
        if not searchId:
            return {
                "status":"FAILED",
                "error":"Id не указан"
            }
        
        for user in tableUsers: 
            if user['id'] == searchId:
                foundUser = user
                break
            
        
        if not foundUser:
            return {
                "status":"FAILED",
                "error":"Не нашлось пользователя с таким логином"
            }
            
        tableUsers.remove(foundUser)
        
        return{
            "status":"OK",
            "error":""
        }
        
api.add_resource(Login, '/login')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)