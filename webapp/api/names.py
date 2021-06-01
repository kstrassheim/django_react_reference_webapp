from django.http import JsonResponse
from django.urls import path, re_path
from asgiref.sync import sync_to_async
import json

urls = [] 

async def get_names(request):
    data = ['George', 'Annie', 'Harley']
    # save to put safe = false on responding arrays
    return await sync_to_async(JsonResponse)(data, safe=False)
urls+=[path('api/names', get_names)]


async def print_name(request):
    # todo encode data
    data = {"param1": request.GET["name"]}
    return await sync_to_async(JsonResponse(data))
urls+=[path('api/print_name', print_name)]

async def print_userid_param(request, user_id):
    # todo encode data
    data = {"userId": user_id}
    return await sync_to_async(JsonResponse(data))
urls+=[re_path(r'^api/print_userid_param/(?P<user_id>\d+)/', print_userid_param)]

# Remark the overloading of string parameter over same url
async def print_username_param(request, user_id):
    # todo encode data
    data = {"userName": user_id}
    return await sync_to_async(JsonResponse)(data)
urls+=[re_path(r'^api/print_userid_param/(?P<user_id>\D+)/', print_username_param)]

# Remark the overloading of string parameter over same url
async def post_username_param(request):
    # todo encode data

    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        data = post_data.get("user")
        print(post_data)
        return await sync_to_async(JsonResponse)(data, safe=False)
    else:
        raise Exception(f"Method {request.method} not allowed")
urls+=[path('api/post_user_param', post_username_param)]


