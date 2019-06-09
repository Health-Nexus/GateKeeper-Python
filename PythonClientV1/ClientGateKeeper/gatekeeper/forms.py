# from django import forms
# from django.db import models
#
# class UploadFileForm(forms.Form):
#     name = models.CharField(max_length=100)
#     file = models.FileField(upload_to="file")
from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = '__all__' # Or a list of the fields that you want to include in your form
