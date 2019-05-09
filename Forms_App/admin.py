# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import C_Details, D_Details,Trashcan1 #,Details

# Register your models here.

#admin.site.register(Details)
admin.site.register(C_Details)
admin.site.register(D_Details)
admin.site.register(Trashcan1)

