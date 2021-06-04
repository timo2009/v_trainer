from django.urls import path

from radioready.views import *
urlpatterns = [
    path('', RadioShowListView.as_view(), name='radio_ready-list')
]
