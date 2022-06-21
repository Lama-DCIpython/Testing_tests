from fastapi import FastAPI, HTTPException
from my_app import controller
app = FastAPI()


@app.get('/client/{id_}')
def get_client(id_):
    client = controller.get_client(id_)
    if client:
        return client
    raise HTTPException(status_code=404)
