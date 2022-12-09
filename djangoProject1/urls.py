"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from energy.views import (service_list, transfer_list, start_list, service_create, service_update, ServiceDetail, ServiceCreate, ServiceUpdate,
    service_detail, ServiceList, confirmation, news_list_json, NewsList, NewsViewSet, DataTransferViewSet)

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'data_transfer', DataTransferViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', start_list, name='start'),
    path('service_list/', ServiceList.as_view(), name='transfer'),
    path('service/confirmation/', confirmation, name='confirm1'),
#    path('service_list/', service_list, name='transfer'),
    path('service/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),
    path('service/<int:pk>/update/', ServiceUpdate.as_view(), name='service_update'),
    #path('service/<int:pk>/update', service_update, name='service_update'),
    #    path('service/<int:pk>/', service_detail, name='service_detail'),
    path('service/create/', ServiceCreate.as_view(), name='ser_create'),
    #path('service/create/', service_create, name='ser_create'),
    path('home/', transfer_list, name='personal_page'),
    path('news/', NewsList.as_view(), name='news'),
    path('news/json/', news_list_json, name='transfer-json'),
    path('service/<int:pk>/create/confirmation/', confirmation, name='confirm1'),
    path('service/<int:pk>/update/confirmation/', confirmation, name='confirm2'),
    path('admin/', admin.site.urls),
#    path('home/', admin.site.urls),
]
