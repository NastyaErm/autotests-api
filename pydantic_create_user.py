from pydantic import BaseModel, EmailStr, Field, constr


class UserSchema(BaseModel):
    """ Модель данных пользователя """
    id: str
    email: EmailStr
    last_name: constr(min_length=1) = Field(alias="lastName")
    first_name: constr(min_length=1) = Field(alias="firstName")
    middle_name: constr(min_length=1) = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """ Запрос на создание пользователя """
    email: EmailStr
    password: constr(min_length=1)
    last_name: constr(min_length=1) = Field(alias="lastName")
    first_name: constr(min_length=1) = Field(alias="firstName")
    middle_name: constr(min_length=1) = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """ Ответ с данными созданного пользователя """
    user: UserSchema

