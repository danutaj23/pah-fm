"""pah_fm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from fleet_management.api import (
    CarListView,
    CurrentUserRetrieveView,
    DriveView,
    PassengerListView,
    ProjectView,
    VerificationTokenView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-token-auth/', obtain_jwt_token),
    path('api/users/me', CurrentUserRetrieveView.as_view(), name='me'),
    path('api/passengers', PassengerListView.as_view(), name='passengers'),
    path('api/cars', CarListView.as_view(), name='cars'),
    path('api/drives', DriveView.as_view(), name='drives'),
    path('api/projects', ProjectView.as_view(), name='projects'),
    path('api/verification-token/<uuid:token>',
         VerificationTokenView.as_view(), name='verification-token')
]
