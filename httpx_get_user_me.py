import httpx

# Данные для входа
login_payload = {
    "email": "user070707@gmail.com",
    "password": "12345qQ"
}

# Выполняем запрос на аутентификацию
login = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=login_payload)

# Получаем JSON-ответ
login_data = login.json()

# Выводим ответ
print("Status code:", login.status_code)
print("Login response:", login_data)

#Получаем accessToken
access_token = login_data["token"]["accessToken"]

#Передаем токен в заголовке
headers = {"Authorization": f"Bearer {access_token}"}

#Получить данные пользователя
get_user_me = httpx.get(url="http://localhost:8000/api/v1/users/me", headers=headers)

#Выводим ответ
print("Status code:", get_user_me.status_code)
print("User response:", get_user_me.json())