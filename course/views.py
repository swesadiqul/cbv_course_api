from django.shortcuts import render
from .models import *
from .serializers import CourseSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import ViewSet, ModelViewSet





class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



'''class CourseViewSet(ViewSet):
    def list(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)'''

# Create your views here.
# CBV operations
# class CourseAPIView(APIView):
#     def get(self, request, format=None):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # CBV operations
# class CourseAPIDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Mixins Non-primary Key Base Operations
# class CourseAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# Mixins Primary Key Base Operations
# class CourseAPIDetail(generics.GenericAPIView, 
#             mixins.RetrieveModelMixin,  
#             mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#             queryset = Course
#             serializer_class = CourseSerializer

#             def get(self, request, *args, **kwargs):
#                 return self.retrieve(request, *args, **kwargs)

#             def put(self, request, *args, **kwargs):
#                 return self.update(request, *args, **kwargs)

#             def delete(self, request, *args, **kwargs):
#                 return self.destroy(request, *args, **kwargs)


# Generic class base non-primary key operation
# class CourseAPIView(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# Generic class base primary key operation
# class CourseAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer