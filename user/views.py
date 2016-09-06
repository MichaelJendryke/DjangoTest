from django.shortcuts import render

from django.http import Http404
from .models import User
import operator #this is to sort objects

# Create your views here.

def index(request):
    user_list = User.objects.order_by('lastname') # use '-' or nothing to sort lastname
    #ordered = sorted(user_list, key=operator.attrgetter('lastname')) #custom order
    context = {
        'user_list': user_list,
    }
    return render(request, 'user/index.html', context)


def detail(request, code):
    try:
        u = User.objects.get(pk=id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'user/detail.html', {'user': u})