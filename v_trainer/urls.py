from django.urls import path

from .views import *


urlpatterns = [

	path('', IndexView.as_view(), name='index'),

	path('lateintest_10_vokabel/create/', LateinTestZehnVokalelCreate.as_view(), name='lateintest_10_vokabel_create'),
	path('lateintest_10_vokabel/update/<pk>/', LateinTestZehnVokalelUpdate.as_view(), name='lateintest_10_vokabel_update'),
	path('lateintest_10_vokabel/detail/<pk>/', LateinTestZehnVokalelDetail.as_view(), name='lateintest_10_vokabel_detail'),
	path('lateintest_1_vokabel/detail/<pk>/', LateinTestZehnVokalelDetail.as_view(), name='lateintest_1_vokabel_detail'),
	path('lateintest_10_vokabel/list/', LateinTestZehnVokalelList.as_view(), name='lateintest_10_vokabel_list'),

	path('englischtest_10_vokabel/create/', EnglischTestZehnVokalelCreate.as_view(), name='englischtest_10_vokabel_create'),
	path('englischtest_10_vokabel/update/<pk>/', EnglischTestZehnVokalelUpdate.as_view(), name='englischtest_10_vokabel_update'),
	path('englischtest_10_vokabel/detail/<pk>/', EnglischTestZehnVokalelDetail.as_view(), name='englischtest_10_vokabel_detail'),
	path('englischtest_10_vokabel/list/', EnglischTestZehnVokalelList.as_view(), name='englischtest_10_vokabel_list'),

	path('deutschtest_10_vokabel/update/<pk>/', DeutschTestZehnVokaleUpdate.as_view(), name='deutschtest_10_vokabel_update'),
	path('deutschtest_10_vokabel/detail/<pk>/', DeutschTestZehnVokaleDetail.as_view(), name='deutschtest_10_vokabel_detail'),
	path('deutschtest_10_vokabel/create/', DeutschTestZehnVokalelCreate.as_view(), name='deutschtest_10_vokabel_create'),
	path('deutschtest_10_vokabel/list/', DeutschTestZehnVokaleList.as_view(), name='deutschtest_10_vokabel_list'),

	path('vokabeltestliste/', vokabeltestliste.as_view(), name='vokabeltestliste'),
	path('Vokabeltrainer_datenschutz/', NutzerDaten.as_view(), name='Vokabeltrainer_datenschutz'),
	path('anleitung/', anleitung.as_view(), name='anleitung'),
	path('neuer_test/', listView.as_view(), name='neuer_test')
]