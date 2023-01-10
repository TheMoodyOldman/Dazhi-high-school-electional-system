from django.urls import path
from .views import *

urlpatterns = [
    path('', ListElections.as_view(), name='mainpage'),
    path('create/', CreateElection.as_view(), name='create_ele'),
    path('ele<int:pk>/', DetailElection.as_view(), name='detail_ele'),
    path('ele<int:pk>/delete/', DeleteView.as_view(), name='delete_ele'),
    path('ele<int:pk>/run/', RunElection.as_view(), name='run_ele'),
    path('ele<int:ele>/candidate<int:pk>/', ElectionBulletin.as_view(), name='candidate'),
    path('ele<int:ele>/candidate<int:pk>/edit', EditElectionBulletin.as_view()
    , name='edit_bulletin'),
    path('ele<int:ele>/candidate<int:pk>/withdraw', ElectionBulletin.as_view()
    , name='candidate_withdraw'),
    path('ele<int:ele>/candidate<int:pk>/vote', Vote.as_view(), name='vote'),
]