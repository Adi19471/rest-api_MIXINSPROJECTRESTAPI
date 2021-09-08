from django.db.models import fields
from django.shortcuts import render
from django.views import generic


from .models import Employe 
from .serializers import EmployeSerializers 


from rest_framework import mixins ,generics

# Create your views here.

class EmployeListView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):

                       queryset = Employe.objects.all()
                       serializer_class = EmployeSerializers

                       def get(self,request):
                           return self.list(request)
                        
                       def post(self,request):
                           return self.create(request)




class EmployeDetaileView(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):

                        queryset = Employe.objects.all()
                        serializer_class = EmployeSerializers





                        def get(self,request,pk):
                            return self.retrieve(request)

                        def put(self,request,pk):
                            return self.update(request)

                        def delete(self,request,pk):
                            return self.destroy(request)    

                    





