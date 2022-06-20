from django.shortcuts import render
from rest_framework import generics, status
# Create your views here
from rest_framework.response import Response


class add(generics.GenericAPIView):

    def post(self,request):
        data = request.data
        if data["first_name"] == "vishal":
            response_dict = {"message":"Hi" + " "+data["first_name"]+" " + data["last_name"]}
        else:
            response_dict = {"message":"Hi user"}
        return Response(response_dict,status=status.HTTP_200_OK)
