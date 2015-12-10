from django.contrib.auth.models import User
from django.db import models

class logdata(models.Model):
    """this class represents the logs Model.
    """
    log_id = models.CharField(max_length=200)
    elapsed_time = models.CharField(max_length=50)
    client_ip = models.CharField(max_length=100)
    username = models.CharField(max_length=400)
    connection_id = models.CharField(max_length=1000)
    date = models.DateTimeField()#CharField(max_length=50)
    time = models.CharField(max_length=50)
    method_url = models.CharField(max_length=2000)
    http_status = models.CharField(max_length=200)
    byte_transferred = models. FloatField()#IntegerField()
    referrer_url = models.CharField(max_length=2000)
    user_agent = models.CharField(max_length=500)
    mime = models.CharField(max_length=500)
    filter_name = models.CharField(max_length=500)
    filter_profile = models.CharField(max_length=1000)
    interface = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.log_id

    class meta:
        ordering = ('created',)