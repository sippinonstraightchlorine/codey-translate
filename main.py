from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()
translator = Translator()

class CeviriIstegi(BaseModel):
    q: str
    source: str
    target: str

@app.post("/translate")
def ceviri_yap(istek: CeviriIstegi):
    try:
        sonuc = translator.translate(istek.q, src=istek.source, dest=istek.target)
        return {"translatedText": sonuc.text}
    except Exception as e:
        return {"error": str(e)}
