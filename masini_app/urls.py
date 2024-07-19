#IN CADRUL ACESTUI FISIER DEFINIM RUTELE APLICATIEI NOASTRE masini
#FISIER CREAT DE NOI CA SA PUTEM DEFINII RUTELE RESPECTIVE DE URL

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path #IMPORTAM DIN DJANGO FUCNTIA DE URL CU PATH
from masini_app.views import home_view, product_upload, ProductListView, product_details

app_name = 'masini_app'

urlpatterns = [
    path('', home_view, name='home'),#Dam doar o referinta nu o apelam  # Numele html ului este numele de home
    #de aceea am scris la name=home sa ii dam o referinta de unde sa ia url ul si html ul
    path('upload_product/', product_upload, name='product_upload'),#Dam o referinta la product_upload
    #Dupa acest pas o sa facem un fisier forms.py in aplicatia noastra masini_app
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:product_id>', product_details, name='product'), #Trebuie prezicat <int:product_id> pentru ca este un numar intreg
    #Si asa acesam un anumit product in url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

