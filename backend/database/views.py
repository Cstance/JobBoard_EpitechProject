import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from .serializer import UserSerializer, AdvertisementSerializer, CompanySerializer, ApplicationSerializer
from .models import Users, Advertisements, Companies, Application

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users
from .serializer import UserSerializer
# Create your views here.


@csrf_exempt
def pwdCheck(request):
    data = JSONParser().parse(request)
    loggin_user = Users.objects.get(email=data.get("email"));

    response_string = '{"token": "", "code": 401, "message": "Could not Authenticate user"}'
    response = json.loads(response_string)

    if loggin_user.check_password(data.get("password")): 
        response["token"] = Token.objects.get_or_create(user=loggin_user)[0].key
        response["code"] = 202
        response["message"] = "Success" 
    return JsonResponse(response)

@csrf_exempt
def isAdvertiser(request):
    data = json.loads(JSONParser().parse(request));
    user = Token.objects.get(key=data.get("token")).user
    response_body = json.loads('{"advertiser": "'+ str(user.advertiser) + '"}')
    return JsonResponse(response_body)

@csrf_exempt
def getInformation(request):
    data = json.loads(JSONParser().parse(request));
    user = Token.objects.get(key=data.get("token")).user
    body = '{"id": "' + str(user.id) + '", "name": "'+ str(user.name) + '", "last_name":"' + str(user.last_name) + '", "email":"' + str(user.email) + '", "phone":"' + str(user.phone) + '", "location":"' + str(user.location) + '"}'

    response_body = json.loads(body)
    return JsonResponse(response_body)




class BaseRequestHandler:
    model = None
    serializer = None

    @csrf_exempt
    def all(self, request):
        if request.method == 'GET':
            items = self.model.objects.all()
            serializer = self.serializer(items, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = self.serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def single(self, request, pk):
        try:
            item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = self.serializer(item)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = self.serializer(item, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            item.delete()
            return HttpResponse(status=204)

class UserRequests(BaseRequestHandler):
    model = Users
    serializer = UserSerializer

    @csrf_exempt
    def all(self, request):
        if request.method == 'GET':
            items = self.model.objects.all()
            serializer = self.serializer(items, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = self.serializer(data=data)
            if serializer.is_valid():
                password = data.get('password')
                user = serializer.save()
                user.set_password(password)
                user.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

class CompanyRequests(BaseRequestHandler):
    model = Companies
    serializer = CompanySerializer

class AdvertisementRequests(BaseRequestHandler):
    model = Advertisements
    serializer = AdvertisementSerializer

class ApplicationRequests(BaseRequestHandler):
    model = Application
    serializer = ApplicationSerializer