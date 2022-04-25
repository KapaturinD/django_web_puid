from django.db import models
import datetime


class Puid(models.Model):
    id = models.BigAutoField('ID', primary_key=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата')
    vehicle_class = models.CharField('Класс', max_length=255)
    zone = models.TextField('zone')
    speed = models.CharField('Скорость', max_length=255)
    length = models.CharField('Габариты', max_length=255)

    def __str__(self):
        return f'Дата: {self.datetime}, ID : {self.id}, vehicle_class: {self.vehicle_class} Точки фиксаций: {self.zone}, Скорость: {self.speed}, Габариты: {self.length}'

    class Meta:
        managed = False
        db_table = 'radar'
        ordering = ['datetime']

