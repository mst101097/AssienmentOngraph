from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework import generics,mixins

# Create your views here.

# this view use for show the student data and create the student data
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


# this view use for the update, delete and retrive the data(we can also create particular view for particular activity)
class StudentDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)