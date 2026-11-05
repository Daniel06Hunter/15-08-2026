from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет от Docker и CI/CD!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}