from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.models import Create_Poll, Create_User
from django.contrib import messages
from .serializer import PollSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


def get_poll_results(request):
    if request.method == 'GET':
        data = request.body
        print(type(data))
        stream = io.BytesIO(data)
        print(type(stream))
        payload = JSONParser().parse(stream)
        print(type(payload))
        id = payload.get('id', None)
        if id is not None:
            poll = Create_Poll.objects.get(id = id)
            print(poll)
            serializer = PollSerializer(poll)
            print(type(serializer.data))
            print(serializer.data)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data, content_type='application/json')
        else:
            polls = Create_Poll.objects.all()
            serializer = PollSerializer(polls, many=True)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data, content_type='application/json')
