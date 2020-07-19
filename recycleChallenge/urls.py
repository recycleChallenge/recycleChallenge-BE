"""recycleChallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from app import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'recycles', views.RecycleViewSet)
router.register(r'recycleItems', views.RecycleItemViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'badReasons', views.BadReasonViewSet)

urlpatterns = [
    url(r'^svg/', views.StaticView.as_view()),
    url(r'^assets/', views.StaticView.as_view()),
    url(r'^$', views.HomePageView.as_view()),
    # url('/', views.HomePageView.as_view()),

    url(r'^accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^users', views.UserEditView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)