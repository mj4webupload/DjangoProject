from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello MAjid,</h1>")