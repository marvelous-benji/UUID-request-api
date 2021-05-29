from uuid import uuid4
from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UUIDGenerator

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
