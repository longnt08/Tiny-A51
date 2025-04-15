from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from services.character_encrypt import A51Cipher as character_cipher
from services.string_encrypt import StringEncrypt as string_cipher
import re
from pydantic import BaseModel


router = APIRouter()

class TinyA51(BaseModel):
    key: str
    plain_text: str
    type: str

@router.post('/Tiny-A51')
def encrypt_character(data: TinyA51):
    try:
        if data.type not in ['encrypt', 'decrypt']:
            raise HTTPException(status_code=400, detail={"message": "type error"})
        
        # tao bang khoa
        key_str = str(data.key).strip()
        key_arr = [int(x) for x in key_str if x in ['0', '1']]

        # print(f"key_str = {repr(key_str)}")
        # print(f"key_arr = {key_arr} ({len(key_arr)} phần tử)")


        if len(key_arr) != 23:
            raise HTTPException(status_code=400, detail={"message": "Khóa mã hóa phải có độ dài là 23."})

        # ma hoa mot ky tu
        if len(data.plain_text) == 1:
            result = character_cipher.encrypt(keyArr=key_arr,character=data.plain_text)

            if not result['status']:
                raise HTTPException(status_code=400, detail=result)

            if data.type == 'encrypt':
                return JSONResponse(status_code=200, content={"status": True, 
                                                                "encrypted_character": result['result_character'], 
                                                                "process_details": result['process_details']})
            
            if data.type == 'decrypt':
                return JSONResponse(status_code=200, content={"status": True,
                                                              "decrypted_character": result['result_character'],
                                                              "process_details": result['process_details']})

        # ma hoa mot chuoi
        if len(data.plain_text) > 1:
            result = string_cipher.encrypt(keyArr=key_arr, string_input=data.plain_text)
            if not result["status"]:
                raise HTTPException(status_code=400, detail=result['message'])
            
            if data.type == 'encrypt':
                return JSONResponse(status_code=200, content={"encrypted_string": result["result_string"], "process_details": result["process_details"], "status": True})
            
            if data.type == 'decrypt':
                return JSONResponse(status_code=200, content={"decrypted_string": result["result_string"], "process_details": result["process_details"], "status": True})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))