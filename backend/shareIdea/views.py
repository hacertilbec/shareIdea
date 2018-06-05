# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from shareIdea.models import *
from shareIdea.serializers import *
from .models import *
from .serializers import *


@csrf_exempt
def userProfile_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = userProfile.objects.all()
        serializer = userProfileSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = userProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
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
<<<<<<< HEAD
def project_list(request):
=======
def projects_list(request):
>>>>>>> origin/master
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

<<<<<<< HEAD
@csrf_exempt
def project_detail(request, pk):
=======

@csrf_exempt
def project_details(request, pk):
>>>>>>> origin/master
    """
    Retrieve, update or delete a code snippet.
    """
    try:
<<<<<<< HEAD
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
=======
        user = Project.objects.get(pk=pk)
    except userProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(user)
>>>>>>> origin/master
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
<<<<<<< HEAD
        serializer = ProjectSerializer(project, data=data)
=======
        serializer = ProjectSerializer(user, data=data)
>>>>>>> origin/master
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
<<<<<<< HEAD
        project.delete()
        return HttpResponse(status=204)
=======
        user.delete()
        return HttpResponse(status=204)


>>>>>>> origin/master
