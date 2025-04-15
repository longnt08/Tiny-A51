from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.encrypt_controller import router as TinyA51_router

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "hello"}

app.include_router(TinyA51_router, prefix="/api", tags=['TinyA5/1'])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)