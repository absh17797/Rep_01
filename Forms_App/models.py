# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


"""
class Details(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Gender = models.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
    Ph_no = models.IntegerField()
    def __str__(self):
	return self.First_Name	
"""
"""------------------------------------------ """
class D_Details(models.Model):

    D_Username = models.CharField(max_length=200)
    D_Password = models.CharField(max_length=200)
    D_Name = models.CharField(max_length=200)
    D_Address = models.CharField(max_length=200)
    D_Ph_no = models.CharField(max_length=11)
    Truck_no = models.CharField(max_length=200)
    def __str__(self):
        return self.D_Name

class C_Details(models.Model):
    C_Username = models.CharField(max_length=200)
    C_Password = models.CharField(max_length=200)
    C_Name = models.CharField(max_length=200)
    C_Address = models.CharField(max_length=200)
    C_Ph_no = models.CharField(max_length=11)
    C_D_id = models.ForeignKey(D_Details, on_delete=models.CASCADE)
    C_Dustbin_ID = models.CharField(max_length=200)
    def __str__(self):
        return self.C_Name

class Trashcan1(models.Model):
    T_ID = models.CharField(max_length=10)
    T_x_c = models.CharField(max_length=14)
    T_y_c = models.CharField(max_length=14)
    T_C_id = models.ForeignKey(C_Details, on_delete=models.CASCADE,default="")
    T_D_id = models.ForeignKey(D_Details, on_delete=models.CASCADE,default="")




""" 
class LogIn(models.Model):
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    As = models.CharField(max_length=7,choices=[('Client','Client'),('Driver','Driver')])
"""