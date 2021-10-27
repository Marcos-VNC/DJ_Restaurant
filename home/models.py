from django.db import models
from django.utils import timezone


# Create your models here.
class Ingrediente(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=4)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Lanche(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=5)
    tipo = models.CharField(max_length=10, default='P',
                             choices=(('P','Pizza'), ('H','Hamburguer'), ('D','Doce'))
                             )
    imagem = models.ImageField(blank=True, upload_to='lanches/%y/%m/%d/')

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    nomeCliente = models.CharField(max_length=30)
    data = models.DateTimeField(default=timezone.now())
    fk_Lanche = models.ForeignKey(Lanche, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.nomeCliente
    
