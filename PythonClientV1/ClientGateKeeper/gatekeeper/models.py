from django.db import models
import json

    #TODO Finalize generic model structure

class Details(models.Model):
    account_number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    days = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.details


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Accounts(models.Model):
    phuse_number = models.CharField(max_length=200)
    public_key = models.CharField(max_length=200)

    def __str__(self):
        return self.phuse_number

class Upload(models.Model):
    fileKey = models.FileField(upload_to="gatekeeper/file")
