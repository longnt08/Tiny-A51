from fastapi import FastAPI
from controller.encrypt_controller import router as TinyA51_router

app = FastAPI(debug=True)

@app.get("/")
def root():
    return {"message": "hello"}

app.include_router(TinyA51_router, prefix="/api", tags=['TinyA5/1'])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)