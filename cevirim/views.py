from django.shortcuts import render
from googletrans import Translator, LANGUAGES
from datetime import datetime

def ceviri_view(request):
    translated_text = None
    detected_lang = None
    diller = list(LANGUAGES.items())

    # Oturumdan geçmiş çevirileri ve sayacı çek
    gecmis = request.session.get("gecmis", [])
    toplam_ceviri = request.session.get("istatistik", 0)

    if request.method == "POST":
        q = request.POST.get("q")
        source = request.POST.get("source")
        target = request.POST.get("target")

        if source == "auto":
            source = "auto"

        translator = Translator()
        try:
            result = translator.translate(q, src=source, dest=target)
            translated_text = result.text
            detected_lang = result.src

            gecmis.append({
                "q": q,
                "source": source,
                "target": target,
                "result": result.text,
                "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M")
            })

            gecmis = gecmis[-5:]
            request.session["gecmis"] = gecmis

            toplam_ceviri += 1
            request.session["istatistik"] = toplam_ceviri

        except Exception as e:
            translated_text = f"Hata: {str(e)}"

    return render(request, "index.html", {
        "result": translated_text,
        "detected_lang": detected_lang,
        "diller": diller,
        "gecmis": gecmis,
        "istatistik": toplam_ceviri
    })
