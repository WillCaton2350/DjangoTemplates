from django.contrib import admin
from django.urls import path, include



urlpatterns = [

        path('', include('HowTo.urls')),

        path('index.html/', include('HowTo.urls')),

        path('about.html/',include('HowTo.urls')),

        path('contact.html/',include('HowTo.urls')),

        path('faq.html/', include('HowTo.urls')),

        path('admin/', admin.site.urls),
        
        ]






