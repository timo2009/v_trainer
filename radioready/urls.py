from django.urls import path
from radioready.views import *
urlpatterns = [
    path('', RadioShowListView.as_view(), name='radio_ready-list'),
    path('radioandenken', RadioAndenken.as_view(), name='radioandenken'),
    path('daten_und_nutzer', RadioAndenken.as_view(), name='radioandenken')

]
