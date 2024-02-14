from fastapi import APIRouter, Response, status
from config.db import con
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()
key = Fernet.generate_key() # Cifrar Password
f = Fernet(key)

@user.get('/users', response_model=list[User], tags=[users]) # Indicamos que es una lista de Users, no un string y el tag, es porque todas pertenecen a la categoria users
def get_users():
    return con.execute(users.select()).fetchall()

@user.post('/users', response_model=User, tags=[users]) # Aquí recibimos un User, todas categoria users, en DOCS lo agrupa por los tags
def create_user(user: User):
    new_user = {'name': user.name, 'email': user.email}
    new_user['password'] = f.encrypt(user.password.encode('utf-8'))
    result = con.execute(users.insert().values(new_user))
    return con.execute(users.select().where(users.c.id == result.lastrowid)).first() # Indicamos la c para indcar la columna que queremos y mostramos el último usuario

@user.get('/users/{id}', response_model=User, tags=[users])
def show_user(id: str):
    return con.execute(users.select().where(users.c.id == id )).first()
    

@user.put('/users/{id}', response_model=User, tags=[users])
def update_user(id: str, user: User):
    con.execute(users.update().values(name = user.name, email = user.email, password=f.encrypt(user.password.encode('utf-8'))).where(users.c.id == id))
    # return "Usuario Update"
    return con.execute(users.select().where(users.c.id == id)).first()

@user.delete('/users/{id}', status_code=HTTP_204_NO_CONTENT, tags=[users])
def delete_user(id: str):
    con.execute(users.delete().where(users.c.id == id))
    # return 'Usuario Eliminado'
    return Response(status_code=HTTP_204_NO_CONTENT) # Devuelve bien, pero no devuelve nada