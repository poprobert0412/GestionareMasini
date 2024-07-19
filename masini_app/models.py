from django.db import models

# Create your models here.

#Vom defini structura bazei de date
#aici scriem structura bazei de date din documentul pe care il avem
#PUNEM SI IMAGINILE DEOARECE AVEM NEVOIE DE ELE
#Vom instala libraria Pillow folosind comanda python pip install Pillow

class Products(models.Model):
    name = models.CharField(max_length=100) # Dam o referinta ca avem voie sa folosim maxim 100 de caractere la nume
    description = models.TextField() #Punem acest .TextField deoarece o sa avem un text la description dar
    # putem folosii cate caractere dorim deoaarece nu am pus max_lenght
    price = models.DecimalField(max_digits=15, decimal_places=2) #Avand un pret am pus maxim 15 numere si 2 decimale
    # dupa virgula
    horse_power = models.PositiveIntegerField(default=0) #Am pus numar normal si de aceea am folosit
    # .PositiveIntegerField am pus si default=0
    available = models.PositiveIntegerField(default=0)
    color = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) #Daca dorim sa atasam imagini atunci
    #o sa ne trebuiasca .ImageField

    def __str__(self):
        return self.name

class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models