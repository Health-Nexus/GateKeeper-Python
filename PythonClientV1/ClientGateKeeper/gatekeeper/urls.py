
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/<str:address_id>/<str:signature>/<str:message_hash>/<str:phuse_number>', views.register, name='data'),
    path('<str:address_id>/<str:signature>/<str:message_hash>/<str:parameter>/<str:key_hex>', views.data, name='data'),


]
