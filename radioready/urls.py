from django.urls import path
from radioready.views import *

urlpatterns = [
    path('', RadioShowListView.as_view(), name='radio_ready-list'),
    path('radioandenken', RadioAndenken.as_view(), name='radioandenken'),
    path('daten_und_nutzer', NutzerDaten.as_view(), name='daten_und_nutzer'),
    path('newsletter', RadioNewsletter.as_view(), name='newsletter'),
    path('songwishes/create/', SongWishesCreate.as_view(), name='songwishes_create'),
    path('songwishes', SongWishesList.as_view(), name='songwishes_list')

]
