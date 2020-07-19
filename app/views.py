from rest_framework import viewsets
from .serializers import *
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, JsonResponse

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

    def get_queryset(self):
        mail = self.request.query_params.get('mail')
        if mail == None:
            return User.objects.all()
        else:
            return User.objects.filter(mail=mail)


class LoginView(TemplateView):
    serializer_class = UserSerializer

    def post(self, request, **kwargs):
        try:
            body = json.loads(request.body)
            user = User.objects.get(mail=body.get('mail'))
            return HttpResponse(user.password == body.get("password"))
        except Exception as ex:
            return HttpResponse(False)


class UserEditView(TemplateView):
    serializer_class = UserSerializer

    def put(self, request, **kwargs):
        body = json.loads(request.body)
        user = User.objects.get(userId=body.get('userId'))
        user.point = body.get('point')
        user.save()
        return JsonResponse({'msg': 'success'})


class RecycleViewSet(viewsets.ModelViewSet):
    queryset = Recycle.objects.all()
    serializer_class = RecycleSerializer

    def get_queryset(self):
        userId = self.request.query_params.get('userId')
        if userId == None:
            return Recycle.objects.all()
        else:
            return Recycle.objects.filter(userId=userId)


class RecycleItemViewSet(viewsets.ModelViewSet):
    queryset = RecycleItem.objects.all()
    serializer_class = RecycleItemSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        recycleId = self.request.query_params.get('recycleId')
        if recycleId == None:
            return Rating.objects.all()
        else:
            return Rating.objects.filter(recycleId=recycleId)


class BadReasonViewSet(viewsets.ModelViewSet):
    queryset = BadReason.objects.all()
    serializer_class = BadReasonSerializer
