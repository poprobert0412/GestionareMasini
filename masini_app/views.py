from django.shortcuts import render, redirect, get_object_or_404
from masini_app.forms import ProductForm
from django.views.generic import ListView
from masini_app.models import Products

# Create your views here.

def home_view(request):
    return render(request, 'masini_app/home.html')

#product_upload este o functie cu ajutorul careia putem sa incarcam produsele folosind un sablon
def product_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)#Accesam pe clasa ProductForm din forms .POST si .FILES TOATE CU LITERE MARI!
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'masini_app/upload_product.html', context={'form': form})
#Am incarcat template ul html upload_product in template si dam o referinta la fisierul acesta ca sa putem acesa pagina html
#Dupa ce am scris functia de mai sus intram in urls.py ca sa scriem cod sa ne afiseze pagina upload_product.html

class ProductListView(ListView): #Importam from django.views.generic import ListView
    #Cu aceasta clasa cream si afisam o lista de obiecte!
    model = Products
    template_name = 'masini_app/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #O sa fie un dictionar care o sa aiba cheia products
        context['products'] = context['object_list']
        return context

def product_details(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request, template_name='masini_app/product.html', context={'product': product})
