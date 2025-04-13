from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from src.services.character_encrypt import A51Cipher


router = APIRouter()

router.post('/character-encrypt')
def encrypt_character(key: str = Form(...),
                      plain_text: str = Form(...),
                      type: str = Form(...)
):
    try:
        if type not in ['encrypt', 'decrypt']:
            raise HTTPException(status_code=400, detail={"message": "type error"})
        if type == 'encrypt':
            return
        if type == 'decrypt':
            pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))