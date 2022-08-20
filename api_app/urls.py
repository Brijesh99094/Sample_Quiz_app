from django.urls import path
from .views import *
urlpatterns = [
    path('',api,name='api'),

    #person api
    path('person-list/',ListPersons,name='person-list'),
    path('person-detail/<int:pk>/',person_detail,name='person-detail'),
    path('person-delete/<int:pk>/',person_delete,name='person-delete'),
    path('person-create/',person_create,name='person-create'),


    # task api
    path('task',TaskApi.as_view(),name='task-api'),
    path('task/<str:pk>/',TaskApi.as_view(),name='task-api')
]