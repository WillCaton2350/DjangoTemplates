from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('contact.html/', views.contact, name='contact'),
    path('about.html/contact.html/faq.html',views.faq, name="faq"),
    path('faq.html/', views.faq, name='faq'),
]