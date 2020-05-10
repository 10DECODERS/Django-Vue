import json
from django.shortcuts import render
from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView)
from user.models import User
from user.serializers import (UserSerializers)
from utils.pagination import CustomPagination

class UserPost(ListAPIView):
    pagination_class = CustomPagination

    def post(self, request, format=None):
        try:
            serializer = UserSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise e

    def get(self, request):
        try:
            queryset = User.objects.filter()
            paginate_queryset = self.paginate_queryset(queryset)
            serializer = UserSerializers(paginate_queryset, many=True)
            return Response({"response": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            raise e

class UserView(APIView):

    def get(self, request, pk, format=None):
        try:
            queryset = get_list_or_404(User, id=pk)
            user_data = UserSerializers(queryset, many=True)
            return Response({"response": user_data.data}, status=status.HTTP_200_OK)
        except Exception as e:
            raise e

    def put(self, request, pk, *args, **kwargs):
        try:
            data = request.data
            inst = User.objects.get(id=pk)
            serializer = UserSerializers(instance=inst, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()                      
                return Response({"response": serializer.data}, status=status.HTTP_200_OK)
            else: 
                return Response({"Success": "false"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            raise e

    def delete(self, request, pk, *args, **kwargs):

        industry= User.objects.get(pk=pk).delete()
        return Response({"response": "deleted"}, status=status.HTTP_200_OK)
