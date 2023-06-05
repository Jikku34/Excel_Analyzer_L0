from django.urls import path
from . import views

# urls for homeapp
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.index, name='home-page'),
    path('student_profile/<str:id>', views.student_profile, name='student_profile'),
    path('remove',views.remove,name='remove'),
    path('show',views.show,name='show')
]