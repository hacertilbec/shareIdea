# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from shareIdea.models import *
from shareIdea.serializers import *

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


def register(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = userProfileSerializer(data=data)
        if serializer.is_valid():
            allUsers = userProfile.objects.all()
            allUserSerializer = userProfileSerializer(allUsers, many=True)
            for i in range(len(allUserSerializer.data)):
                if allUserSerializer.data[i]["email"]==serializer.data["email"] and allUserSerializer.data[i]["password"]==serializer.data["password"]:
                    return JsonResponse(allUserSerializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
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
def project_list(request):
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


def show_users(request):
    all_users = userProfile.objects.all()
    template = '<html>'
    for user in all_users:
        template += str(user) + '<br><pre>    - My Projects: '
        for project in user.my_projects.all():
            template += str(project) + ', '
        template += '<pre>'
        template += '<pre>    - Other Projects: '
        for project in user.other_projects.all():
            template += str(project) + ', '
        template += '<pre><br><br>'
    template += '</html>'
    return HttpResponse(template)


def user_register(reqeust, name, surname):
    user_1 = userProfile(name=name, surname=surname)
    user_1.save()
    all_users = userProfile.objects.all()
    return HttpResponse(all_users)


def project_create(request, title, owner):
    owner = userProfile.objects.get(name=owner)
    owner.my_projects.create(title=title)
    return HttpResponse(Project.objects.all())


def project_participate(request, title, participant):
    participant = userProfile.objects.get(name=participant)
    project = Project.objects.get(title=title)
    participant.other_projects.add(project)
    return HttpResponse(Project.objects.all())
