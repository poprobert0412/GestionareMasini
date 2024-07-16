#IN CADRUL ACESTUI FISIER DEFINIM RUTELE APLICATIEI NOASTRE masini
#FISIER CREAT DE NOI CA SA PUTEM DEFINII RUTELE RESPECTIVE DE URL

from django.urls import path #IMPORTAM DIN DJANGO FUCNTIA DE URL CU PATH
from masini_app.views import home_view

app_name = 'masini_app'

urlpatterns = [
    path('', home_view, name='home')#Dam doar o referinta nu o apelam  # Numele html ului este numele de home
    #de aceea am scris la name=home sa ii dam o referinta de unde sa ia url ul si html ul
]