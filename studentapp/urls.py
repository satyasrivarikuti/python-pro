from django.urls import path
from . import views

app_name = 'studentapp'
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('studentHomePage/', views.StudentHomePage, name='studentHomePage'),
    path('view_marks/', views.view_marks, name='view_marks'),
]
