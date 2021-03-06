"""DDTProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views
from django.urls import path


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.main_page, name='main_page'),
    path('udo-view/', views.udo_view, name='udo_view'),
    path('staff/', views.staff_view, name='staff'),
    path('create-team-view/', views.create_team_view, name='create_team_view'),
    path('result-participation-view/', views.result_participation_view, name='result_participation_view'),
    path('union-interes-view/', views.union_interes_view, name='union_interes_view'),
    path('info-about-personal-view/', views.info_about_personal_view, name='info_about_personal_view'),
    path('npa/', views.npa_view, name='npa_view'),
    path('metodic-events-view/', views.metodic_events_view, name='metodic_events_view'),
    path('support-platform/', views.support_platform_view, name='support_platform'),
    path('map/', views.map_view, name='map'),
    path('list-organizations/', views.list_organization_view, name='list_organization_view'),

]
