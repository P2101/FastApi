from pydantic import BaseModel
from typing import Optional

# Para Validar los datos de entrada y salida en las solicitudes HTTP
class User(BaseModel): 
    id: Optional[str]
    name: str
    email: str
    password: str
