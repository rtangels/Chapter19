from django.urls import path

from catalog.views import contact,homepage

urlpatterns = [
    path('',homepage),
    path('',contact),
]