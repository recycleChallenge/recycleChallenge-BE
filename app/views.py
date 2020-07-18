from rest_framework import viewsets
from .serializers import *
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class StaticView(TemplateView):
    def get(self, request, **kwargs):
        response = redirect('/static/' + request.path)
        return response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RecycleViewSet(viewsets.ModelViewSet):
    queryset = Recycle.objects.all()
    serializer_class = RecycleSerializer


class RecycleItemViewSet(viewsets.ModelViewSet):
    queryset = RecycleItem.objects.all()
    serializer_class = RecycleItemSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class BadReasonViewSet(viewsets.ModelViewSet):
    queryset = BadReason.objects.all()
    serializer_class = BadReasonSerializer
