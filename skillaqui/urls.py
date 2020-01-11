from django.urls import path
from . import views
from .views import signupview


urlpatterns = [
    path('index/', views.index,name='index'),
    path('course/', views.course,name='course'),
    path('about/', views.about,name='about'), 
    path('landing/', views.landing,name='landing'),
    path('services/', views.services,name='services'),
    path('product_details/<slug:slug>/', views.details,name='details'),
    path('videos/', views.videos,name='videos'),
    # path('logout/', views.logout,name='logout'),
    path('signup/',signupview.as_view(),name='signup'),
    path('commentpage/<slug:slug>/',views.commentpage,name='commtentpage'),

    
]

  