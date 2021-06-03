from django.urls import path

from .views import *


urlpatterns = [

	path('', IndexView.as_view(), name='index'),
	path('englischtest_1_vokabel/create/', EnglischTestEineVokalelCreate.as_view(), name='englischtest_1_vokabel_create'),
	path('englischtest_1_vokabel/update/<pk>/', EnglischTestEineVokalelUpdate.as_view(), name='englischtest_1_vokabel_update'),
	path('englischtest_1_vokabel/detail/<pk>/', EnglischTestEineVokalelDetail.as_view(), name='englischtest_1_vokabel_detail'),
	path('engschtest_1_vokabel/list/', EnglischTestEineVokalelList.as_view(), name='englischtest_1_vokabel_list'),
	path('deutschtest_1_vokabel/create/', DeutschTestEineVokalelCreate.as_view(), name='deutschtest_1_vokabel_create'),
	path('deutschtest_1_vokabel/update/<pk>/', DeutschTestEineVokalelUpdate.as_view(), name='deutschtest_1_vokabel_update'),
	path('deutschtest_1_vokabel/detail/<pk>/', DeutschTestEineVokalelDetail.as_view(), name='deutschtest_1_vokabel_detail'),
	path('deutschtest_1_vokabel/list/', DeutschTestEineVokalelList.as_view(), name='deutschtest_1_vokabel_list'),
	path('vokabeltestliste/', vokabeltestliste.as_view(), name='vokabeltestliste'),
	path('anleitung/', anleitung.as_view(), name='anleitung'),
	path('neuer_test/', listView.as_view(), name='neuer_test'),
	path('radio_ready/', RadioReady.as_view(), name='radio_ready')



]