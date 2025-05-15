from django.urls import path
from . import views
from .views import robots_txt, sitemap_xml

urlpatterns = [
    path("", views.ceviri_view, name="ceviri"),
    path("robots.txt", robots_txt, name="robots"),
    path("sitemap.xml", sitemap_xml, name="sitemap"),
]
