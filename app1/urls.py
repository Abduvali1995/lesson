from django.urls import path
from .views import first_view,second_view,three_view,four_view

urlpatterns =  [
    path('', first_view, name = 'first-view'),
    path('second-view/', second_view, name='second-view'),
    path('3-view/', three_view, name='second-view'),
    path('4-view/', four_view, name='second-view')
]
