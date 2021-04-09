from django.urls import path
from . import views
from Remedy1.views import fieldDesc

app_name = "Remedy1"

urlpatterns = [
    path('', views.index, name='index' ),
    path('inherit/', views.inherit, name='inherit' ),
    path('sendEmail/', views.sendEmail, namespace='sendEmail' ),
    path('contactUs/', views.contactUs, namespace='contact' ),
    
    #LOGIN and LOGOUT
    path('login/', views.log, name='login' ),
    path('logOut/', views.logOutUser, name='logOut' ),

    #Upload
    path('upload/', views.upLoad, name='upload' ),

    #delete Upload
    path('delete/<str:pk>/', views.delete, name='delete' ),
    path('delSuccess/', views.delSuccess, name='delSuccess' ),

    path('products/', views.products, name='products' ),

    #FIELD VIEW
    path('field/', views.field, name='field'),
    
    #PRODUCST MANY
    path('elegance/', views.eleganceView, name='elegance' ),
    path('arrow/', views.arrowView, name='arrow' ),
    path('dene/', views.deneView, name='dene' ),
    path('dazzle/', views.dazzleView, name='dazzle' ),
    path('lily/', views.lilyView, name='lily' ),
    path('ZigZag/', views.zigView, name='ZigZag' ),

    #Description Of Product
    path('fieldDesc/<str:pk>/', fieldDesc.as_view(), name= 'fieldDesc' ),

    path('aboutUs/', views.about, name='about' ),
]