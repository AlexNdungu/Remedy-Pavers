from django.forms import ModelForm
from .models import Upload

#UPLOAD PAGE FORM 

class UploadForm(ModelForm):
    class Meta():
        model = Upload
        fields = '__all__'
