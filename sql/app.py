from fastapi import FastAPI
from routes.user import user

# Esto se ve en DOCS
app = FastAPI(
    title='My first API',
    description='Cualquier cosa',
    version='0.0.1',
    openapi_tags=[{
        'name':'users',
        'description': 'Users Routes'
    }]
) 
app.include_router(user)

