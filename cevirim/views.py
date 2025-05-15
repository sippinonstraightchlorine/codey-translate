from django.shortcuts import render
from googletrans import Translator, LANGUAGES
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.http import require_GET

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


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://codeytranslate.xyz/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

@require_GET
def sitemap_xml(request):
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://codeytranslate.xyz/</loc>
      <changefreq>weekly</changefreq>
      <priority>1.0</priority>
   </url>
</urlset>
"""
    return HttpResponse(content, content_type="application/xml")
