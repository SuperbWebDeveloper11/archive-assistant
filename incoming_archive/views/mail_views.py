from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
# import models
from ..models import Mail
from ..filters import MailFilter
from ..forms import MailForm # we'll use this form to create and update instance


"""
function based views (hardcoded) to perform crud operations for ajax requests
    1- mail_list (render mail list template)
    - the following methods will respond to JQuery ajax requests -
    2- mail_detail (return mail detail template)
    3- mail_create (return mail create template && save new mail)
    4- mail_update (return mail update template && update mail)
    5- mail_delete (return mail delete template && delete mail)
"""


def mail_list(request): 
    """ render mail list template """

    template_list = 'incoming_archive/mail/mail_list.html'
    mail_list = Mail.objects.all()
    mail_list_filter = MailFilter(request.GET, queryset=mail_list)
    context = {'mail_list_filter': mail_list_filter, 'mail_form': MailForm()}
    return render(request, template_list, context)


def mail_detail(request, pk):
    """ return mail detail template """

    template_error = 'incoming_archive/mail/partial_error_msg.html'
    template_detail = 'incoming_archive/mail/partial_mail_detail.html'

    if not request.user.is_authenticated: # user should be logged in
        context = {"error_msg": "Please login"}
        error_temp = render_to_string(template_error, context, request=request)
        return JsonResponse({'modal_temp': error_temp})
    else:
        try:
            # return partial_mail_detail template 
            instance = Mail.objects.get(pk=pk)
            context = { 'mail': instance }
            detail_temp = render_to_string(template_detail, context, request=request)
            return JsonResponse({'modal_temp': detail_temp})
        except: # propably mail not found
            error_temp = render_to_string(template_error, request=request)
            return JsonResponse({'modal_temp': error_temp})


def mail_create(request):
    """ return mail create template && save new mail """

    template_error = 'incoming_archive/mail/partial_error_msg.html'
    template_create = 'incoming_archive/mail/partial_mail_create.html'
    template_list = 'incoming_archive/mail/partial_mail_list.html'

    if not request.user.is_authenticated: # user should be logged in
        context = {"error_msg": "Please login"}
        error_temp = render_to_string(template_error, context, request=request)
        return JsonResponse({'modal_temp': error_temp})
    else:
        if request.method == 'GET':
            # return partial_mail_create template with an empty form to create instance 
            context = {'form': MailForm()}
            create_temp = render_to_string(template_create, context, request=request)
            return JsonResponse({'modal_temp': create_temp})
        elif request.method == 'POST':
            form = MailForm(request.POST, request.FILES)
            if form.is_valid(): 
                # save the instance and return partial list template 
                form.instance.created_by = request.user
                form.save() 
                mail_list = Mail.objects.all()
                context = {'mail_list': mail_list}
                list_temp = render_to_string(template_list, context, request=request)
                return JsonResponse({'list_temp': list_temp, 'form_is_valid': True})
            else:
                # return partial create template with a form populated with the data previously submitted 
                context = {'form': form}
                create_temp = render_to_string(template_create, context, request=request)
                return JsonResponse({'modal_temp': create_temp, 'form_is_valid': False})


def mail_update(request, pk):
    """ return mail update template && update mail """

    template_error = 'incoming_archive/mail/partial_error_msg.html'
    template_update = 'incoming_archive/mail/partial_mail_update.html'
    template_list = 'incoming_archive/mail/partial_mail_list.html'

    if not request.user.is_authenticated: # user should be logged in
        context = {"error_msg": "Please login"}
        error_temp = render_to_string(template_error, context, request=request)
        return JsonResponse({'modal_temp': error_temp})
    else:
        if request.method == 'GET':
            try:
                # return partial_mail_update template with bounded form 
                instance = Mail.objects.get(pk=pk)
                if request.user != instance.created_by: # the user should be the one who created the mail 
                    raise
                context = {'form': MailForm(instance=instance)}
                update_temp = render_to_string(template_update, context, request=request)
                return JsonResponse({'modal_temp': update_temp})
            except: # propably mail not found
                error_temp = render_to_string(template_error, request=request)
                return JsonResponse({'modal_temp': error_temp})
        elif request.method == 'POST':
            try:
                instance = Mail.objects.get(pk=pk)
                if request.user != instance.created_by: # the user should be the one who created the mail 
                    raise
                form = MailForm(request.POST, request.FILES, instance=instance)
                if form.is_valid(): 
                    # save the instance and return partial list template 
                    form.save() 
                    mail_list = Mail.objects.all()
                    context = {'mail_list': mail_list}
                    list_temp = render_to_string(template_list, context, request=request)
                    return JsonResponse({'list_temp': list_temp, 'form_is_valid': True})
                else:
                    # return partial update template with a form populated with the data previously submitted 
                    context = {'form': form}
                    update_temp = render_to_string(template_update, context, request=request)
                    return JsonResponse({'modal_temp': update_temp, 'form_is_valid': False})
            except: # propably mail not found
                error_temp = render_to_string(template_error, request=request)
                return JsonResponse({'modal_temp': error_temp})


def mail_delete(request, pk):
    """ return mail delete template && delete mail """

    template_error = 'incoming_archive/mail/partial_error_msg.html'
    template_delete = 'incoming_archive/mail/partial_mail_delete.html'
    template_list = 'incoming_archive/mail/partial_mail_list.html'

    if not request.user.is_authenticated: # user should be logged in
        context = {"error_msg": "Please login"}
        error_temp = render_to_string(template_error, context, request=request)
        return JsonResponse({'modal_temp': error_temp})
    else:
        if request.method == 'GET':
            try:
                # return partial_mail_delete template with bounded form 
                instance = Mail.objects.get(pk=pk)
                if request.user != instance.created_by: # the user should be the one who created the mail 
                    raise
                context = {'form': MailForm(instance=instance)}
                delete_temp = render_to_string(template_delete, context, request=request)
                return JsonResponse({'modal_temp': delete_temp})
            except: # propably mail not found
                error_temp = render_to_string(template_error, request=request)
                return JsonResponse({'modal_temp': error_temp})
        elif request.method == 'POST':
            try:
                # delete the instance and return partial list template 
                instance = Mail.objects.get(pk=pk)
                if request.user != instance.created_by: # the user should be the one who created the mail 
                    raise
                instance.delete()
                mail_list = Mail.objects.all()
                context = {'mail_list': mail_list}
                list_temp = render_to_string(template_list, context, request=request)
                return JsonResponse({'list_temp': list_temp, 'form_is_valid': True})
            except: # propably mail not found
                error_temp = render_to_string(template_error, request=request)
                return JsonResponse({'modal_temp': error_temp})
 

