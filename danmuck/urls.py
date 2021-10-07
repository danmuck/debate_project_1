"""danmuck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contact_view, ev_tracker_view, postal_view, about_view
from toodoo.views import all_toodoo_view, new_toodoo_view, toodoo_editor, main_toodoo_view, delete_toodoo_view

#SCHOOL
from debate_project.views import all_ev_view, new_ev_view, main_ev_view, delete_ev_view, ev_editor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('ev_tracker/', ev_tracker_view, name='ev_tracker'),
    path('postal/', postal_view, name='postal'),
    path('about/', about_view, name='about'),

#todo
    path('todo/', main_toodoo_view, name='todo'),
    path('list/', all_toodoo_view, name='list'),
    path('new/', new_toodoo_view, name='new'),
    path('editor/<int:toodoo_id>/', toodoo_editor, name='editor'),
    path('delete/<int:toodoo_id>/', delete_toodoo_view, name='delete'),
#apps
    path('products/', include('products.urls')),
    path('postal/', include('postal.urls')),


#SCHOOL

    path('ev_home/', main_ev_view, name='ev_home'),
    path('evidence/', all_ev_view, name='evidence'),
    path('new_ev/', new_ev_view, name='ev_new'),
    path('ev_editor/<int:ev_id>/', ev_editor, name='ev_editor'),
    path('delete_ev/<int:ev_id>/', delete_ev_view, name='ev_delete'),





]
