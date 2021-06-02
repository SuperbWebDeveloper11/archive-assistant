from django.urls import include, path
from .views import mail_views


app_name = 'incoming_archive'


urlpatterns = [

    ####################### urls for 'mails' curd operations using JQuery #######################
    path('mail/', mail_views.mail_list, name='mail_list'),
    path('mail/add/', mail_views.mail_create, name='mail_add'),
    path('mail/<int:pk>/detail/', mail_views.mail_detail, name='mail_detail'),
    path('mail/<int:pk>/update/', mail_views.mail_update, name='mail_update'),
    path('mail/<int:pk>/delete/', mail_views.mail_delete, name='mail_delete'),

]


