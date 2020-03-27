from django.db import models


# Create your models here.

class Trip(models.Model):
    class Meta:
        db_table = 'trip'
        ordering = ['-id']

    classification_types = (
        (0, 'Trabalho'),
        (1, 'Atividade física'),
        (2, 'Lazer'),
        (3, 'Deslocamento')
    )

    owner = models.ForeignKey('auth.User', related_name='trips', on_delete=models.CASCADE)
    start_date = models.DateTimeField('Data Inicio', blank=True, null=True)
    end_date = models.DateTimeField('Data Fim', blank=True, null=True)
    classification = models.IntegerField(choices=classification_types, blank=True, null=True)
    rating = models.IntegerField('Nota', blank=True, null=True)

    def __str__(self):
        return 'self.classificacao'
