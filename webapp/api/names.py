from django.http import JsonResponse
from django.urls import path, re_path

urls = [] 

def get_names(request):
    data = ['George', 'Annie', 'Harley']
    # save to put safe = false on responding arrays
    return JsonResponse(data, safe=False)
urls+=[path('api/names', get_names)]


def print_name(request):
    # todo encode data
    data = {"param1": request.GET["name"]}
    return JsonResponse(data)
urls+=[path('api/print_name', print_name)]

def print_userid_param(request, user_id):
    # todo encode data
    data = {"userId": user_id}
    return JsonResponse(data)
urls+=[re_path(r'^api/print_userid_param/(?P<user_id>\d+)/', print_userid_param)]

# Remark the overloading of string parameter over same url
def print_username_param(request, user_id):
    # todo encode data
    data = {"userName": user_id}
    return JsonResponse(data)
urls+=[re_path(r'^api/print_userid_param/(?P<user_id>\D+)/', print_username_param)]

# Remark the overloading of string parameter over same url
def post_username_param(request):
    # todo encode data
    data = {"user": request.POST["user"]}
    return JsonResponse(data)
urls+=[path('api/post_user_param', post_username_param)]


