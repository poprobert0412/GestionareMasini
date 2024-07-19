#Importam forms ul complet din django
from django import forms
from masini_app.models import Products
#In cadrul acestui fisier vom crea toate clasele necesare pentru formulare personalizate

#Includem o clasa Meta in clasa ProductForm cu referinta la forms.ModelForm din framework ul django
#Este important sa introducem clasa Meta in clasa noastra Product form

class ProductForm(forms.ModelForm):
    class Meta: #Aceasta clasa ne ajuta pe noi sa modelam FORMULARUL uploud_products care o sa fie vizual
        model = Products #Facem referire la formularul pentru produsele din baza de date din models.py din clasa Products
        #In field ul de mai jos indorducem din models.py numele coloanelor din baza de date
        fields = [#Aici scriem coloanele din baza de date, numele coloanelor le putem afla din models.py
            'name',
            'description',
            'price',
            'horse_power',
            'available',
            'color',
            'image'
        ]
