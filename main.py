from fastapi import FastAPI

##creo una instancia de mi clase
app=FastAPI()
@app.get("/")#Este es mi endpoint raíz
def prueba():
    return{"mensaje":"Mi API está funcionando" }