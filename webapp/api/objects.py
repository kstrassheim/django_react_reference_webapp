from django.http import JsonResponse
from django.urls import path

urls = [] 
# handle custom objects
from django.db import models
# class CustomObject(models.Model):
#     question = models.CharField(max_length=100)
#     date = models.DateTimeField(auto_now=True)
#     def __str__(self): return self.question


def print_obj(request, param1:int, param2):
    # custom_object_instance = get_object_or_404(CustomObject, pk=param2)
    # data = {"results": {
    #     "question": custom_object_instance.question,
    #     "pub_date": custom_object_instance.date
    # }}
    return JsonResponse("")
urls+=[path('api/objects', print_obj)]