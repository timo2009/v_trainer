from django.urls import path
from radioready.views import *

urlpatterns = [
    path('', RadioShowListView.as_view(), name='radio_ready-list'),
    path('radioandenken', RadioAndenken.as_view(), name='radioandenken'),
    path('daten_und_nutzer', NutzerDaten.as_view(), name='daten_und_nutzer'),
    path('newsletter', RadioNewsletter.as_view(), name='newsletter'),
    path('songwishes/create/', SongWishesCreate.as_view(), name='songwishes_create'),
    path('songwishes', SongWishesList.as_view(), name='songwishes_list'),
    path('radioshow/detail/<pk>/', RadioShowDetail.as_view(), name='radioshow_detail'),
    path('style', StyleCss.as_view(), name='style'),

    path('kommentar/create/', KommentareCreate.as_view(), name='kommentar_create'),
    path('kommentar/update/<pk>', KommentareUpdate.as_view(), name='kommentar_update'),
    path('kommentare', KommentareList.as_view(), name='kommentare_list'),

]