from django.urls import path
from .views import AnnounceList, MyAnnounces, ResponsesList, AnnounceCreate, AnnounceUpdate, AnnounceDelete,\
    ResponseDelete, ResponseCreate, ResponseAccept, Mailing


urlpatterns = [
    path('', AnnounceList.as_view(), name='home'),
    path('announce/<int:pk>', ResponsesList.as_view(), name='responses_list'),
    path('myannounces/', MyAnnounces.as_view(), name='my_announces'),
    path('create/', AnnounceCreate.as_view(), name='announce_create'),
    path('announce/<int:pk>/recreate', ResponseCreate.as_view(), name='response_create'),
    path('announce/<int:pk>/update/', AnnounceUpdate.as_view(), name='announce_update'),
    path('announce/<int:pk>/delete/', AnnounceDelete.as_view(), name='announce_delete'),
    path('response/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete'),
    path('response/<int:pk>/accept/', ResponseAccept.as_view(), name='response_accept'),
    path('mailing/', Mailing.as_view(), name='mailing'),

]
