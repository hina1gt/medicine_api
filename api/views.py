from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import *
from first.models import *

class ClientAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        return [permissions.IsAdminUser()]

    def get(self, request, *args, **kwargs):
        client = self.get_queryset().all()
        serializer = self.get_serializer(client, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class ClientDetailAPI(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        return [permissions.IsAdminUser()]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SponsorAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
        

    def get(self, request, *args, **kwargs):
        sponsor = self.get_queryset().all()
        serializer = self.get_serializer(sponsor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class SponsorDetailAPI(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]
            
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class BlogAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
        

    def get(self, request, *args, **kwargs):
        blog = self.get_queryset().all()
        serializer = self.get_serializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class BlogDetailAPI(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]
            
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)