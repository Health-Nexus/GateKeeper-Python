
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:address_id>/<str:signature_id>/<str:message_hash>/<str:parameter>/<str:key>', views.data, name='data'),

]
