from django.test import TestCase

# Create your tests here.

import requests

def ceviri_yap(metin, kaynak_dil, hedef_dil):
    url = "http://localhost:5050/translate"
    veri = {
        "q": metin,
        "source": kaynak_dil,
        "target": hedef_dil,
        "format": "text"
    }
    try:
        response = requests.post(url, data=veri)
        print("Status code:", response.status_code)
        print("Yanıt:", response.text)
    except Exception as e:
        print("Hata:", str(e))

ceviri_yap("Merhaba dünya", "tr", "en")

# Amk bu test olayı ÇOK ÖNEMLİYMİŞ hatayı buldum çeviri sitesindeki
# python tests.py ile çalıştırdım ve aşağıda hatayı verdi ve net anladım ChatGPT ile yarım saattir çözmeye çalışıyorduk.
