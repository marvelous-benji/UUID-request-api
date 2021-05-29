from uuid import uuid4
from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UUIDGenerator


'''
We have taken this approach as it is more efficient and
continues to return response quickly and effectively.
If we had gone with the standard way of creating a
timefield and uuidfield in the models.py file and then
use a serializer to get the stored data, we would still
have to convert it to a dict with time as key and uuid as
values, which would require us to loop through and perform
those conversion for each item in the dict, this would
work properly for small request, but when the requests
increases, we would have slow response.So we simply
made use of the idea that:
x = '{"a":"b"}'
'{' + '"c":"d"'+','+ x[1:] = '{"c":"d","a":"b"}'
and with the function eval, we can convert our result to 
a dictionary
'''

class UUIDView(APIView):
#creates an empty dictionary on first request if it does not exist
    def initialize_dict(self):
        first_dict = UUIDGenerator.objects.first()
        if not first_dict:
            return UUIDGenerator.objects.create()
        return first_dict

    def get(self,request):
        dict_object = self.initialize_dict()
        response = dict_object.cached_response
        unique_id = uuid4().hex
        time = datetime.now()
        dict_object.cached_response = '{'+f'"{time}":"{unique_id}"'+','+ response[1:]
        dict_object.save()
        return Response(eval(dict_object.cached_response),status=status.HTTP_200_OK)

    
 
