from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('', HomePage, name='HomePage'),
    path('login', LoginPage, name='LoginPage'),
    path('register', SignupPage, name='SignupPage'),
    path('logout', UserLogout, name='UserLogout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)