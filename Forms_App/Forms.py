from django import forms
from . models import C_Details ,D_Details,Trashcan1



"""
class ContactForm(forms.Form):
	First_Name = forms.CharField()
	Last_Name = forms.CharField()
	Address = forms.CharField(widget=forms.Textarea)
	Gender = forms.ChoiceField(choices=[('M','Male'),('F','Female')])
	Ph_no = forms.IntegerField()

class DetailsForm(forms.ModelForm):
	class Meta:
		model = Details
		fields = ('First_Name','Last_Name','Address','Gender','Ph_no')
"""
"""	 ----------------------------------------------------------
class Driver_Form(forms.Form):
	D_Username = forms.CharField(max_length=200)
	D_Password = forms.CharField(max_length=200)
	D_Name = forms.CharField(max_length=200)
	D_Address = forms.CharField(max_length=200)
	D_Ph_no = forms.CharField(max_length=200)
	Truck_no = forms.CharField(max_length=200)
"""
class D_Form(forms.ModelForm):
	class Meta:
		model = D_Details
		fields = ('D_Username','D_Password','D_Name','D_Address','D_Ph_no','Truck_no')
"""
class Customer_Form(forms.Form):
    C_Username = forms.CharField(max_length=200)
    C_Password = forms.CharField(max_length=200)
    C_Name = forms.CharField(max_length=200)
    C_Address = forms.CharField(max_length=200)
    C_Ph_no = forms.CharField(max_length=200)
    C_D_id = forms.CharField(max_length=200)
    C_Dustbin_ID = forms.CharField(max_length=200)

"""
class C_Form(forms.ModelForm):
	class Meta:
		model = C_Details
		fields = ('C_Username', 'C_Password', 'C_Name', 'C_Address', 'C_Ph_no', 'C_D_id','C_Dustbin_ID')


class T_Form(forms.ModelForm):
	class Meta:
		model = Trashcan1
		fields = ('T_ID', 'T_x_c', 'T_y_c','T_C_id','T_D_id')

