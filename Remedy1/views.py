from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .decorators import unauthenticaited_user
from .forms import UploadForm
from .models import *

# Create your views here.

def inherit(request):
    return render(request, 'inherit.html')

def index(request):
    return render(request, 'index.html')

def sendEmail(request):
    return render(request, 'email.html')    

def contactUs(request):
    return render(request, 'contact.html')    


#LOGIN PART
@unauthenticaited_user
def log(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('Remedy1:upload')
        else:
            messages.info(request, 'Username Or Password Is INCORRECT!!!')

    return render(request, 'login.html') 


#LOGOUT USER
def logOutUser(request):
    logout(request)
    return redirect('login')    

#LOGIN REQUIRED
@login_required(login_url='login')
def upLoad(request):

    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('field')

    context = {'form':form}

    return render(request, 'adm/upload.html',context )  



#Delete Upload
@login_required(login_url='login')
def delete(request, pk):
    uploadView = Upload.objects.get(id_upload = pk )
    if request.method == 'POST':
        uploadView.delete()
        return redirect('delSuccess')

    context = {'uploadView':uploadView}
    return render(request, 'adm/deleteUp.html',context )    

@login_required(login_url='login')
def delSuccess(request):
    return render(request, 'adm/deleteSuc.html' )



def products(request):
    return render(request, 'products.html')   


def field(request):
   return render(request, 'field.html')

 


"""ALL THE PRODUCTS ON THE FIELD"""
def eleganceView(request):

    allProd = Upload.objects.all()
    elegances = allProd.filter(prod_name='Elegance Shape')

    context = {'elegances':elegances}

    return render(request, 'field/elegance.html',context) 

def arrowView(request):

    allProd = Upload.objects.all()
    Arrow = allProd.filter(prod_name='Arrow Shape')

    context = {'Arrow':Arrow}

    return render(request, 'field/arrow.html',context) 

def deneView(request):

    allProd = Upload.objects.all()
    Dene = allProd.filter(prod_name='Dene Shape')

    context = {'Dene':Dene}

    return render(request, 'field/dene.html',context) 

def dazzleView(request):

    allProd = Upload.objects.all()
    Dazzle = allProd.filter(prod_name='Dazzle Shape')

    context = {'Dazzle':Dazzle}

    return render(request, 'field/dazzle.html',context) 

def lilyView(request):

    allProd = Upload.objects.all()
    lily = allProd.filter(prod_name='Lily Tiles')

    context = {'lily':lily}

    return render(request, 'field/lily.html',context)  

def zigView(request):

    allProd = Upload.objects.all()
    zigs = allProd.filter(prod_name='ZigZag Shape')

    context = {'zigs':zigs}

    return render(request, 'field/ZigZag.html',context)                   

"""ALL THE PRODUCTS DESCRIPTION"""





class fieldDesc(DetailView):
    model = Upload
    template_name = 'field/description.html'
    context_object_name = 'imageDesc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productUp = Upload.objects.get(pk=self.kwargs.get('pk'))

        return context


def about(request):

    testis = Testimonials.objects.all() 

    context = {'testis':testis}   

    return render(request, 'about.html', context)   


#ERROR HANDLING
def error_404(request, exception):
    return render(request, 'error/404.html', status=404)          