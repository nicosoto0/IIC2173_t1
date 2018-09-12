from django.db import models
from django.urls import reverse
#django.urls  was before django.core.urlresolvers
# Create your models here.

class Message(models.Model):
    content = models.CharField(max_length=300)
    ip_client = models.CharField(max_length=50)
    ip_mac = models.CharField(max_length=50)
    request_time =models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('msg_detail',kwargs={'pk': self.pk})

    def __str__(self):
        return (self.content + ' - ' + self.ip_client + ' - ' +  self.request_time)
