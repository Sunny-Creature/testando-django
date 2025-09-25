from django.db import models

# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=250)
    imagem = models.ImageField(upload_to="media/")
    data_public = models.DateField(auto_now_add=True)
    hora_public = models.TimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="avatar/")
    user = models.CharField(max_length=10)
    nome_perfil = models.CharField(max_length=20)