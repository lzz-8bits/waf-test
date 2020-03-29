from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path(r'index',views.index,name='index'),

    path(r'showlog',views.show_log,name='show'),

    path(r'nodelist',views.nodelist,name='node'),

    path(r'login',views.login,name='login'),

    path('logout',views.logout,name='logout'),

    path(r'download',views.conf_download,name='conf_download'),

    path(r'confdisplay',views.conf_display)

]