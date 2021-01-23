from django.urls import path

from . import views
from .views.vokalbeltest_englisch_1_vokabel import EnglischTestEineVokalelCreate, EnglischTestEineVokalelUpdate, EnglischTestEineVokalelList

urlpatterns = [
	# path('', views.index, name='index'),
	# path('deutschtest/', views.deutschtest, name='deutschtest'),
	# path('test/', views.test, name='test'),
	path('englischtest_1_vokabel/create/', EnglischTestEineVokalelCreate.as_view(), name='englischtest_1_vokabel_create'),
	path('englischtest_1_vokabel/update/<pk>/', EnglischTestEineVokalelUpdate.as_view(), name='englischtest_1_vokabel_update'),
	path('englischtest_1_vokabel/list/', EnglischTestEineVokalelList.as_view(), name='englischtest_1_vokabel_list')
]