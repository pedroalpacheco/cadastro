from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    #email = models.email()
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name
