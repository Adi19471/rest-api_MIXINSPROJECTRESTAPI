from django.db import models
from django.db.models import fields
from rest_framework import serializers 
from .models import Employe

class EmployeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employe 
        fields = '__all__'