# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import models
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .Forms import D_Form,C_Form,T_Form #,ContactForm,DetailsForm

from .models import D_Details,C_Details,Trashcan1
from django.contrib import messages

from ubidots import apiclient

"""

def Detail(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			First_Name = form.cleaned_data['First_Name']
			Last_Name = form.cleaned_data['Last_Name']
    			Address =form.cleaned_data['Address']
    			Gender =form.cleaned_data['Gender']
    			Ph_no = form.cleaned_data['Ph_no']
			print(First_Name,Last_Name)
	form = ContactForm()
	return render(request,'form.html',{'form':form})
"""
"""
def Details_Detail(request):
	if request.method == 'POST':
	 form = DetailsForm(request.POST)
	 if form.is_valid():
	  print("Valid")
	  form.save()
	 else:
	  print("InVALID")
	form = DetailsForm()
	return render(request,'form.html',{'form':form})

"""
""" ---------------++++++++ REGISTER CUSTOMER DRIVERS DUSTBINS +++++++++------------------ """
def Customer(request):
	if request.method == 'POST':
		form1 = C_Form(request.POST)
		if form1.is_valid():
			print("Valid")
			messages.success(request, "Recorded Successfully !!")
			form1.save()

		else:
			print("InVALID")

	form1 = C_Form()
	return render(request, 'form.html',{'form1': form1})

def Driver(request):
	if request.method == 'POST':
		form2 = D_Form(request.POST)
		if form2.is_valid():
			print("Valid")
			messages.success(request, "Recorded Successfully !!")
			form2.save()
		else:
			print("InVALID")

	form2 = D_Form()
	return render(request, 'form.html', {'form2': form2})

def Trashcan(request):
	if request.method == 'POST':
		form3 = T_Form(request.POST)
		if form3.is_valid():
			print("Valid")
			messages.success(request, "Recorded Successfully !!")
			form3.save()
		else:
			print("InVALID")

	form3 = T_Form()
	return render(request, 'form.html', {'form3': form3})




""" ------------------  ++++++++++++ DRIVERS LIST DETAIL DELETE ++++++++++++++  --------------------- """


def Driver_list(request):
	alldrivers=D_Details.objects.all()
	context = {'alldrivers':alldrivers}
	return render(request,'List.html',context)



def Driver_Detail(request,id=None):
	driver = get_object_or_404(D_Details,id=id)
	context={'driver':driver}
	return render(request,'D_Detail.html',context)

def Delete_Driver(request,id=None):
	driver=get_object_or_404(D_Details,id=id)
	Name=driver.D_Name
	driver.delete()
	context = {'driver': driver,'D_Name':Name}
	messages.success(request, "Post Successfully Deleted!!!")
	return render(request,'Delete.html',context)

	return HttpResponseRedirect("/list")


""" ------------------  +++++++++++++ CUSTOMERS LIST DETAIL DELETE  +++++++++++++  --------------------- """

def Customer_list(request):
	allcustomers = C_Details.objects.all()
	context = {'allcustomers':allcustomers}
	return render(request,'C_List.html',context)

def Customer_Detail(request,id=None):
	#drivers = get_object_or_404(D_Details,id=id)

	customer = get_object_or_404(C_Details,id=id)
	context={'customer':customer}
	return render(request,'C_Detail.html',context)

def Delete_Customer(request,id=None):
	customer=get_object_or_404(C_Details,id=id)
	Name = customer.C_Name
	customer.delete()
	context = {'customer': customer,'C_Name':Name}
	messages.success(request, "Post Successfully Deleted!!!")
	return render(request,'C_Delete.html',context)
	return HttpResponseRedirect("/C_List")

""" ------------------  +++++++++++++ TRASH CANS  LIST DETAIL DELETE  +++++++++++++  --------------------- """

def Trash_List(request):
	trash = Trashcan1.objects.all()
	customer = C_Details.objects.all()
	driver = D_Details.objects.all()
	#context = {'customer':customer, 'driver':driver}
	context = {'trash':trash, 'customer':customer, 'driver':driver}
	return render(request,'T_List.html',context)



def Trash_Detail(request,id=None):
	trash = get_object_or_404(Trashcan1,id=id)
	customer = C_Details.objects.all()
	driver = D_Details.objects.all()
	context={'trash':trash,'customer':customer,'driver':driver}
	return render(request,'T_Detail.html',context)

def Delete_Trash(request,id=None):
	trash=get_object_or_404(Trashcan1,id=id)
	id=trash.id
	trash.delete()
	context = {'trash': trash,'id':id}
	messages.success(request, "Post Successfully Deleted!!!")
	return render(request,'Delete.html',context)
	return HttpResponseRedirect("/T_list")

""" ------------------  +++++++++++++ TRASH CANS  Maps +++++++++++++  --------------------- """

def Maps(request):
	trash = Trashcan1.objects.all()
	context = {'trash':trash}
	return render(request,'Map.html',context)

def Ubidots(request):
	#data = get_object_or_404(Trashcan1,id=id)
	api = apiclient(token='f9iP6BpxpviO06EbebukACqEZcQMtM')
	value = api.get_variable('5cc1a2ea5916360d3c633d88')
	data = Trashcan1.objects.all()
	context = { 'data': data , 'value':value}
	return render(request,'abc.html',context)

def Multi_map(request):
	trash = Trashcan1.objects.all() #.values_list('T_x_c')
	#trash = Trashcan1.objects.all()
	context = {'trash': trash}
	return render(request,'Multi_map.html',context)

""" ------------------  +++++++++++++ Ubidots +++++++++++++  --------------------- """


