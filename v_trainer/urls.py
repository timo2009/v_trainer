from django.urls import path

from .views import *

urlpatterns = [

	path('', IndexView.as_view(), name='index'),
	path('englischtest_1_vokabel/create/', EnglischTestEineVokalelCreate.as_view(), name='englischtest_1_vokabel_create'),
	path('englischtest_1_vokabel/update/<pk>/', EnglischTestEineVokalelUpdate.as_view(), name='englischtest_1_vokabel_update'),
	path('englischtest_1_vokabel/list/', EnglischTestEineVokalelList.as_view(), name='englischtest_1_vokabel_list'),
]