# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from shareIdea.models import *
from shareIdea.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

@csrf_exempt
def userProfile_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = userProfile.objects.all()
        serializer = userProfileSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def registerUser(request):
    data = JSONParser().parse(request)
    print data
    serializer = userProfileSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    print serializer.errors
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def userProfile_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = userProfile.objects.get(pk=pk)
    except userProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = userProfileSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = userProfileSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def loginUser(request):
    data = JSONParser().parse(request)
    email_ = data["email"]
    password = data["password"]
    print email_
    try:
        user = userProfile.objects.get(email=email_)
        print user.password
        if user.password == password:
            userid = user.id
            return JsonResponse({'id':userid, 'status_code': 200})
        else:
            print "error1"
            return JsonResponse({'id':9999, 'status_code': 400})
    except:
        print "error2"
        return JsonResponse({'id':9999,'status_code': 400})

# @api_view(['POST'])
# class LoginUserView(APIView):
#     renderer_classes = (JSONRenderer,)

#     def get(self, request, format=None):
#         data = JSONParser().parse(request)
#         email_ = data["email"]
#         password = data["password"]
#         try:
#             user = userProfile.objects.get(email=email_)
#             if user.password == password:
#                 userid = user.id
#                 print Response({'id':userid, 'status_code': 400})
#                 return Response({'id':userid, 'status_code': 400})
#             else:
#                 print "error1"
#                 return Response({'status_code': 400})
#         except:
#             print "error2"
#             return Response({'status_code': 400})



@csrf_exempt
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def addProject(request):
    data = JSONParser().parse(request)
    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def project_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status=204)




# def project_participate(request, title, participant):
#     participant = userProfile.objects.get(name=participant)
#     project = Project.objects.get(title=title)
#     participant.other_projects.add(project)
#     return HttpResponse(Project.objects.all())







    