from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def lgoin_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("login success")
        else:
            # Return a 'disabled account' error message
            return HttpResponse("login fail")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("login fail")


def logout_view(request):
    logout(request)

@login_required
def my_view(request):
    return HttpResponse("my_view")
    # if not request.user.is_authenticated():
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

from .models import Question



@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)