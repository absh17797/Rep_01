from django.conf.urls import url,include

from .views import Driver_list, Driver_Detail,Delete_Driver,Customer,Driver,Customer_list,Customer_Detail,Delete_Customer,Trash_List,Trash_Detail,Delete_Trash,Trashcan,Maps,Ubidots,Multi_map
urlpatterns = [

    #url(r'^$', view, name='view'),
    #url('login/', views.login.as_view(), name='login'),

    url(r'^Driver/$', Driver, name='Drivers'),
    url(r'^Clients/$', Customer, name='Customer'),
    url(r'^TrashCans/$', Trashcan, name='Trashcan'),

    url(r'^D_list/$', Driver_list, name='D_List'),
    url(r'^D_list/(?P<id>\d+)/$', Driver_Detail, name='Driver_Detail'),
    url(r'^D_list/$', Delete_Driver, name='Delete_Driver'),

    url(r'^C_list/$', Customer_list, name='Customer_List'),
    url(r'^C_list/(?P<id>\d+)/$', Customer_Detail, name='Customer_Detail'),
    url(r'^C_list/(?P<id>\d+)/delete/$', Delete_Customer, name='Delete_Customer'),

    url(r'^T_list/$', Trash_List, name='Trashcan_List'),
    url(r'^T_list/(?P<id>\d+)/$',Trash_Detail, name='Customer_Detail'),
    url(r'^T_list/(?P<id>\d+)/delete/$', Delete_Trash, name='Delete_Customer'),

    url(r'^Maps/$', Maps, name='Maps'),
    url(r'^Ubidots/$', Ubidots, name='Ubidots'),
    url(r'^Multi_map/$', Multi_map, name='Multi_map'),
]
