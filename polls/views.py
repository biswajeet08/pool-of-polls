from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Create_Poll, Create_User
from django.contrib import messages
from .serializer import PollSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt




@login_required(login_url='/polls/login/')
def pool(request):
    user = request.user
    return render(request, 'polls/pool.html', {'user': user})


def homepage(request):
    user = request.user
    return render(request, 'polls/pool-homepage.html', {'user': user})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gender']
        passwd1 = request.POST['passwd1']
        passwd2 = request.POST['passwd2']

        if passwd1 == passwd2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect("/polls/register/")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email ALREADY EXIST")
                return redirect("/polls/register/")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email,
                                                password=passwd1)
                user.save();
                create_user = Create_User(dob=dob, gender=gender, user=user)
                create_user.save();
                messages.info(request, "REGISTERED")
                return redirect("/polls/register/")
        else:
            messages.info(request, "Password Not Matching")
            return redirect("/polls/register/")

    else:
        return render(request, 'polls/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pword']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/polls/pool/")
        else:
            messages.info(request, "Inavlid Credentials")
            return redirect("/polls/login/")
    else:
        return render(request, 'polls/login.html')


def logout(request):
    auth.logout(request)
    return redirect("/polls/")


@login_required(login_url='/polls/login/')
def sports(request):
    user = request.user
    poll = Create_Poll.objects.filter(category='Sports')

    return render(request, 'polls/sports.html', {'user': user, 'range': range(1, 5), 'poll': poll})


@login_required(login_url='/polls/login/')
def bolly(request):
    user = request.user
    poll = Create_Poll.objects.filter(category='Bollywood')

    return render(request, 'polls/bolly.html', {'user': user, 'range': range(1, 5), 'poll': poll})


@login_required(login_url='/polls/login/')
def misc(request):
    user = request.user
    poll = Create_Poll.objects.filter(category='Misc')

    return render(request, 'polls/misc.html', {'user': user, 'range': range(1, 5), 'poll': poll})


@login_required(login_url='/polls/login/')
def tech(request):
    user = request.user
    poll = Create_Poll.objects.filter(category='Technology')

    return render(request, 'polls/tech.html', {'user': user, 'range': range(1, 5), 'poll': poll})


@login_required(login_url='/polls/login/')
def results(request, poll_id):
    user = request.user
    poll = Create_Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        option = request.POST['choice']
        if option == 'choice1':
            poll.count1 += 1
        elif option == 'choice2':
            poll.count2 += 1
        elif option == 'choice3':
            poll.count3 += 1
        elif option == 'choice4':
            poll.count4 += 1
        poll.save()
    poll = Create_Poll.objects.get(pk=poll_id)
    poll.total = poll.count1 + poll.count2 + poll.count3 + poll.count4
    poll.percent1 = (poll.count1 / poll.total) * 100
    poll.percent2 = (poll.count2 / poll.total) * 100
    poll.percent3 = (poll.count3 / poll.total) * 100
    poll.percent4 = (poll.count4 / poll.total) * 100
    poll.save()

    poll = Create_Poll.objects.all()

    return render(request, 'polls/results.html', {'user': user, 'range': range(1, 5), 'poll': poll})


def result(request):
    user = request.user
    poll = Create_Poll.objects.all()

    return render(request, 'polls/results.html', {'user': user, 'range': range(1, 5), 'poll': poll})


@login_required(login_url='/polls/login/')
def create_poll(request):
    user = request.user
    if request.method == 'POST':

        question = request.POST['question']
        choice1 = request.POST['choice1']
        choice2 = request.POST['choice2']
        choice3 = request.POST['choice3']
        choice4 = request.POST['choice4']
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']
        img4 = request.FILES['img4']
        category = request.POST['category']
        poll = Create_Poll.objects.create(heading=question,
                                          item1=choice1,
                                          item2=choice2,
                                          item3=choice3,
                                          item4=choice4,
                                          img1=img1,
                                          img2=img2,
                                          img3=img3,
                                          img4=img4,
                                          category= category,
                                          count1=0, count2=0, count3=0, count4=0, total=0, percent1=0, percent2=0,
                                          percent3=0,
                                          percent4=0)

        poll.save

        return render(request, 'polls/pool.html', {'user': user})
    else:
        return render(request, 'polls/create_poll.html', {'user': user})

@csrf_exempt
def poll_create_api(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = PollSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Poll Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')



