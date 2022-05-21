from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# # Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello MAjid,</h1>")
default_data ={
    'app_name' : 'nearin_app',
    'no_header_pages' : ['personal_profile','address_profile','admin_index','shop_list','about_us','contact_us','change_shop_password','change_password','index','register_page','profile_page','user_profile2','otp_page','index2','login','register','login_user','user_register']
}

def index(request):
    default_data['current_page'] = 'index'
    # role()
    return render(request, 'index/index.html',default_data)

def register(request):
    default_data['current_page'] = 'register'
    # role()
    return render(request, 'index/register.html',default_data)

def profiles(request):
    print(request.POST)
    
    request.session['user_data'] = {
        'role': request.POST['role'],
        # 'password': request.POST['password'],
    }
    Role.objects.create(
        Role = request.POST['role'],
    )
    return redirect(index)

# def user_data(request):
#     # role = Role.objects.get(Role = request.session['role'])
#     # ro = Profile.objects.get(Master = master)
#     role.Role = request.POST['role']
#     role.Role.save()

#     return redirect(index)
#     # default_data['user_data'] = role