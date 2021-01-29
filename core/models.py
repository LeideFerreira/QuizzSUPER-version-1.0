from django.db import models


# Create your models here.

class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Question(BaseModel):
    pergunta = models.TextField('Pergunta')
    correta = models.CharField('Questao correta', max_length=1)
    solucao = models.TextField('solucao')
    nivel = models.IntegerField('nivel')
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()

    def __str__(self):
        return self.pergunta
