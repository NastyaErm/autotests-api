from http import HTTPStatus
from clients.authentication.authentication_client import get_authentication_client
from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

def test_login():

    #создаем клиентов для работы с пользователем и авторизацией
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    #создаем пользователя
    create_request = CreateUserRequestSchema()
    #запрос на создание пользователя
    public_users_client.create_user(create_request)

    #запрос на логин
    login_request = LoginRequestSchema(
        email=create_request.email,
        password=create_request.password
    )
    #логин
    login_response = authentication_client.login_api(login_request)
    #десериализация ответа
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    #проверка статус-кода
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    # проверяем содержимое ответа
    assert_login_response(login_response_data)

    # валидируем JSON Schema
    validate_json_schema(login_response.json(),
                         login_response_data.model_json_schema())




