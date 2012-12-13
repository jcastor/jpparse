from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Method(models.Model):
	name = models.CharField(max_length=5000)
	signature = models.CharField(max_length=400)
class Class(models.Model):
	name = models.CharField(max_length=5000)
	methods = models.ManyToManyField(Method, blank=True, null=True)
class Variable(models.Model):
	name = models.CharField(max_length=400)
	signature = models.CharField(max_length=400)
	method = models.ForeignKey(Method)
class GlobalVariable(models.Model):
	name = models.CharField(max_length=400)
	signature = models.CharField(max_length=400)
	classowner = models.ForeignKey(Class)
class CodeSegment(models.Model):
	stack = models.IntegerField()
	local = models.IntegerField()
	args_size = models.IntegerField()
	length = models.IntegerField()
	method = models.ForeignKey(Method)

class MethodAdmin(admin.ModelAdmin):
	search_fields = ["name"]
class ClassAdmin(admin.ModelAdmin):
	search_fields = ["name"]
class VariableAdmin(admin.ModelAdmin):
	search_fields = ["name"]
class GlobalVariableAdmin(admin.ModelAdmin):
	search_fields = ["name"]
class CodeSegmentAdmin(admin.ModelAdmin):
	search_fields = ["method"]



