from django.db import models
from datetime import datetime

'''
* livro(titulo)
* resenha
* se ja finalizou o livro
'''

class Livro(models.Model):
    titulo = models.TextField(max_length=50)
    finalizado = models.BooleanField(default=False)
    resenha = models.TextField(max_length=255)
