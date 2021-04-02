from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticaited_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('upload')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func    
