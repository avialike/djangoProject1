from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_service_count(self):
        return self.service_set.all().count()

    class Meta:
        ordering = ['name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Service(models.Model):
    user_service = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    personal_account = models.CharField(max_length=255)

    class Meta:
        ordering = ['user_service']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('service_update', kwargs={'pk': self.pk})

    def get_last_value(self):
        last_value = Data_transfer.objects.order_by('-date').values('value')[:1]
        return(last_value)


class Data_transfer(models.Model):
    user_transfer = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['user_transfer']
        verbose_name = 'Показания'
        verbose_name_plural = 'Показания'

    #def __str__(self):
        #return self.user_transfer

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now)
    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title




