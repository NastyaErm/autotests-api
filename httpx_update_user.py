import httpx
from tools.fakers import get_random_email

#Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user = httpx.post(url="http://localhost:8000/api/v1/users", json=create_user_payload)
create_new_user = create_user.json()
print("Create user: ", create_new_user)
print("Status code: ", create_user.status_code)

#Проходим аутентификацию
login = {
    "email" : create_user_payload['email'],
    "password" : create_user_payload['password']
}
login_user = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=login)
login_new_user = login_user.json()
print("Login data: ", login_new_user)
print("Status code: ", login_user.status_code)

#Обновляем пользователя
patch_user_headers = {
    "Authorization": f"Bearer {login_new_user['token']['accessToken']}"
}
new_data = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
patch_user = httpx.patch(url=f"http://localhost:8000/api/v1/users/{create_new_user['user']['id']}",
                         json=new_data, headers=patch_user_headers)
patch_new_user=patch_user.json()
print("Patch user: ", patch_new_user)
print("Status code: ", patch_user.status_code)
