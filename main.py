from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"msg":"Remote Self Audit project Web service"}
